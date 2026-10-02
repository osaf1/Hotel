function searchRooms() {

    const checkin = document.getElementById("checkin").value;
    const checkout = document.getElementById("checkout").value;
    const occupancy = document.getElementById("occupancy").value;
    const rooms = document.getElementById("rooms").value;

    // Check-in controleren
    if (checkin === "") {
        alert("Please select a check-in date.");
        return;
    }

    // Check-out controleren
    if (checkout === "") {
        alert("Please select a check-out date.");
        return;
    }

    // Occupancy controleren
    if (occupancy === "") {
        alert("Please select the number of guests.");
        return;
    }

    // Aantal kamers controleren
    if (rooms === "") {
        alert("Please select the number of rooms.");
        return;
    }

    // Check-out moet na check-in zijn
    if (checkout <= checkin) {
        alert("Check-out date must be after the check-in date.");
        return;
    }

    // Naar de rooms pagina
    window.location.href = "/rooms";
}


/* =========================
   Language
========================= */

function changeLanguage() {

    alert("Language selection will be added later.");

}


/* =========================
   Room images
========================= */

function changeRoomImage(image) {

    const card = image.closest(".room-card");

    const mainImage = card.querySelector(".room-main-image img");

    mainImage.src = image.src;

}


/* =========================
   Image zoom
========================= */

function openImage(imageSource) {

    const modal = document.getElementById("imageModal");

    const zoomedImage = document.getElementById("zoomedImage");

    zoomedImage.src = imageSource;

    modal.style.display = "flex";

}


/* =========================
   Close image zoom
========================= */

function closeImage() {

    const modal = document.getElementById("imageModal");

    modal.style.display = "none";

}


/* =========================
   Room Details images
========================= */

function changeDetailsImage(image) {

    document.getElementById("mainRoomImage").src = image.src;

}


/* =========================
   Room Details image zoom
========================= */

function openRoomDetailsImage(src) {

    document.getElementById(
        "roomDetailsZoomedImage"
    ).src = src;

    document.getElementById(
        "roomDetailsModal"
    ).style.display = "flex";

}


/* =========================
   Close Room Details zoom
========================= */

function closeRoomDetailsImage() {

    document.getElementById(
        "roomDetailsModal"
    ).style.display = "none";

}

