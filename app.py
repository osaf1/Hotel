from flask import Flask, render_template, request, session, redirect, url_for
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# =========================
# Flask session
# =========================

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
# Room Details
# =========================

@app.route("/room/<int:room_id>")
def room_details(room_id):

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
        "room_details.html",
        room=room
    )


# =========================
# Login
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    # Kamer bewaren als gebruiker
    # vanaf een kamer naar login gaat
    room_id = request.args.get("room_id")

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM users
            WHERE email = %s
        """, (email,))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        # Wachtwoord controleren
        if user and check_password_hash(
            user["password"],
            password
        ):

            session["logged_in"] = True
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            # Als er een kamer geselecteerd was
            if room_id:

                return redirect(
                    url_for(
                        "booking",
                        room_id=room_id
                    )
                )

            # Anders naar rooms
            return redirect(
                url_for("rooms")
            )

        return "Invalid email or password."

    return render_template(
        "login.html",
        room_id=room_id
    )


# =========================
# Register / Join
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")
        postcode = request.form.get("postcode")
        city = request.form.get("city")
        password = request.form.get("password")

        # Wachtwoord hashen
        hashed_password = generate_password_hash(
            password
        )

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Controleren of email bestaat
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

        # Nieuwe gebruiker toevoegen
        cursor.execute("""
            INSERT INTO users
            (
                name,
                email,
                password,
                address,
                postcode,
                city
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            name,
            email,
            hashed_password,
            address,
            postcode,
            city
        ))

        connection.commit()

        # ID van nieuwe gebruiker
        user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        # Automatisch inloggen
        session["logged_in"] = True
        session["user_id"] = user_id
        session["user_name"] = name

        # Naar rooms
        return redirect(
            url_for("rooms")
        )

    return render_template(
        "register.html"
    )


# =========================
# Booking
# =========================

@app.route("/booking")
def booking():

    # Alleen ingelogde gebruikers
    if not session.get("logged_in"):

        room_id = request.args.get("room_id")

        return redirect(
            url_for(
                "login",
                room_id=room_id
            )
        )

    # Geselecteerde kamer
    room_id = request.args.get("room_id")

    if not room_id:
        return redirect(
            url_for("rooms")
        )

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


# =========================
# Booking Confirmation
# =========================

@app.route(
    "/booking-confirmation",
    methods=["GET", "POST"]
)
def booking_confirmation():

    # Alleen ingelogde gebruikers
    if not session.get("logged_in"):

        return redirect(
            url_for("login")
        )

    # Formuliergegevens
    room_id = request.values.get("room_id")
    checkin = request.values.get("checkin")
    checkout = request.values.get("checkout")
    guests = request.values.get("guests")
    number_of_rooms = request.values.get("rooms")

    # Kamer controleren
    if not room_id:

        return "No room selected.", 400

    # Datums controleren
    if not checkin or not checkout:

        return (
            "Please select check-in "
            "and check-out dates.",
            400
        )

    # Checkout moet na checkin zijn
    if checkout <= checkin:

        return (
            "Check-out date must be "
            "after check-in date.",
            400
        )

    # Guests en rooms controleren
    if not guests or not number_of_rooms:

        return (
            "Please select guests "
            "and rooms.",
            400
        )

    # Database verbinding
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Kamer ophalen
    cursor.execute("""
        SELECT *
        FROM rooms
        WHERE id = %s
    """, (room_id,))

    room = cursor.fetchone()

    if not room:

        cursor.close()
        connection.close()

        return "Room not found.", 404

    # =========================
    # Booking opslaan
    # =========================

    if request.method == "POST":

        cursor.execute("""
            INSERT INTO bookings
            (
                user_id,
                room_id,
                checkin,
                checkout,
                guests,
                rooms
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            session["user_id"],
            room_id,
            checkin,
            checkout,
            guests,
            number_of_rooms
        ))

        connection.commit()

        # ID van booking
        booking_id = cursor.lastrowid

        cursor.close()
        connection.close()

        # Confirmation pagina
        return render_template(
            "confirmation.html",
            booking_id=booking_id,
            room=room,
            checkin=checkin,
            checkout=checkout,
            guests=guests,
            rooms=number_of_rooms
        )

    # =========================
    # GET
    # =========================

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


# =========================
# Confirmation
# =========================

@app.route("/confirmation")
def confirmation():

    return render_template(
        "confirmation.html"
    )


# =========================
# Logout
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("home")
    )
    # =========================
# Language
# =========================

@app.route("/language/<language>")
def change_language(language):

    allowed_languages = ["en", "nl", "fa", "ps"]

    if language in allowed_languages:
        session["language"] = language

    return redirect(request.referrer or url_for("home"))


# =========================
# Start Flask
# =========================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5001
    )