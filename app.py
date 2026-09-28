from flask import Flask, render_template, request, session, redirect, url_for
from database import get_db_connection

app = Flask(__name__)

# Session secret key
app.secret_key = "jarir-hotel-secret-key"


# =========================
# Home
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# Rooms
# =========================

@app.route("/rooms")
def rooms():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM rooms
        WHERE available = TRUE
    """)

    rooms = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "rooms.html",
        rooms=rooms
    )


# =========================
# Login
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    # Room bewaren als gebruiker eerst moet inloggen
    room_id = request.args.get("room_id")

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM users
            WHERE email = %s AND password = %s
        """, (email, password))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            session["logged_in"] = True
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            # Als er een kamer was geselecteerd,
            # ga terug naar die kamer
            if room_id:
                return redirect(
                    url_for("booking", room_id=room_id)
                )

            # Als er geen kamer was geselecteerd,
            # ga naar rooms
            return redirect(url_for("rooms"))

        return "Invalid email or password."

    return render_template(
        "login.html",
        room_id=room_id
    )

    # GET
    if request.method == "GET":
        return render_template("login.html")


    # POST
    email = request.form.get("email")
    password = request.form.get("password")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM users
        WHERE email = %s AND password = %s
    """, (email, password))

    user = cursor.fetchone()

    cursor.close()
    connection.close()


    # User found
    if user:

        session["logged_in"] = True
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]

        # After login go to booking
        return redirect(url_for("booking"))


    # Wrong login
    return "Invalid email or password."


# =========================
# Register / Join
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    # GET
    if request.method == "GET":
        return render_template("register.html")


    # Get form information
    name = request.form.get("name")
    email = request.form.get("email")
    address = request.form.get("address")
    postcode = request.form.get("postcode")
    city = request.form.get("city")
    password = request.form.get("password")


    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)


    # Check if email already exists
    cursor.execute("""
        SELECT id
        FROM users
        WHERE email = %s
    """, (email,))

    existing_user = cursor.fetchone()


    if existing_user:

        cursor.close()
        connection.close()

        return "This email is already registered."


    # Create user
    cursor.execute("""
        INSERT INTO users
        (name, email, password, address, postcode, city)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        name,
        email,
        password,
        address,
        postcode,
        city
    ))


    connection.commit()

    # Get new user's ID
    user_id = cursor.lastrowid

    cursor.close()
    connection.close()


    # Remember user
    session["logged_in"] = True
    session["user_id"] = user_id
    session["user_name"] = name


    # After Join go to booking
    return redirect(url_for("booking"))


# =========================
# Booking
# =========================

@app.route("/booking")
def booking():

    if not session.get("logged_in"):
        room_id = request.args.get("room_id")

        return redirect(
            url_for("login", room_id=room_id)
        )

    room_id = request.args.get("room_id")

    if not room_id:
        return redirect(url_for("rooms"))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM rooms
        WHERE id = %s
    """, (room_id,))

    room = cursor.fetchone()

    cursor.close()
    connection.close()

    if not room:
        return "Room not found.", 404

    return render_template(
        "booking.html",
        room=room,
        room_id=room_id
    )

    # User must be logged in
    if not session.get("logged_in"):
        return redirect(url_for("login"))


    # Get selected room
    room_id = request.args.get("room_id")


    # If no room was selected
    if not room_id:
        return "No room selected.", 400


    # Get room from database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM rooms
        WHERE id = %s
    """, (room_id,))

    room = cursor.fetchone()

    cursor.close()
    connection.close()


    # Room does not exist
    if not room:
        return "Room not found.", 404


    return render_template(
        "booking.html",
        room=room,
        room_id=room_id
    )


# =========================
# Booking confirmation
# =========================

@app.route("/booking-confirmation", methods=["GET", "POST"])
def booking_confirmation():

    # User moet ingelogd zijn
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    room_id = request.values.get("room_id")
    checkin = request.values.get("checkin")
    checkout = request.values.get("checkout")
    guests = request.values.get("guests")
    number_of_rooms = request.values.get("rooms")

    if not room_id:
        return "No room selected", 400

    if not checkin or not checkout:
        return "Please select check-in and check-out dates.", 400

    if checkout <= checkin:
        return "Check-out date must be after check-in date.", 400

    if not guests or not number_of_rooms:
        return "Please select guests and rooms.", 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Room ophalen
    cursor.execute(
        "SELECT * FROM rooms WHERE id = %s",
        (room_id,)
    )

    room = cursor.fetchone()

    if not room:
        cursor.close()
        connection.close()
        return "Room not found", 404

    # Als gebruiker op Confirm Booking klikt
    if request.method == "POST":

        sql = """
            INSERT INTO bookings
            (user_id, room_id, checkin, checkout, guests, rooms)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            session["user_id"],
            room_id,
            checkin,
            checkout,
            guests,
            number_of_rooms
        )

        cursor.execute(sql, values)
        connection.commit()

        booking_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return render_template(
            "confirmation.html",
            booking_id=booking_id,
            room=room,
            checkin=checkin,
            checkout=checkout,
            guests=guests,
            rooms=number_of_rooms
        )

    cursor.close()
    connection.close()

    return render_template(
        "booking_confirmation.html",
        room=room,
        room_id=room_id,
        checkin=checkin,
        checkout=checkout,
        guests=guests,
        rooms=number_of_rooms
    )

    # User must be logged in
    if not session.get("logged_in"):
        return redirect(url_for("login"))


    room_id = request.args.get("room_id")
    checkin = request.args.get("checkin")
    checkout = request.args.get("checkout")
    guests = request.args.get("guests")
    number_of_rooms = request.args.get("rooms")


    # Check room
    if not room_id:
        return "No room selected.", 400


    # Get room
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM rooms
        WHERE id = %s
    """, (room_id,))

    room = cursor.fetchone()

    cursor.close()
    connection.close()


    if not room:
        return "Room not found.", 404


    return render_template(
        "booking_confirmation.html",
        room=room,
        checkin=checkin,
        checkout=checkout,
        guests=guests,
        rooms=number_of_rooms
    )


# =========================
# Confirmation
# =========================

@app.route("/confirmation")
def confirmation():

    return render_template("confirmation.html")


# =========================
# Logout
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =========================
# Start Flask
# =========================

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )