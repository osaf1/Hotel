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


  // Rooms controleren
  if (rooms === "") {
      alert("Please select the number of rooms.");
      return;
  }


  // Controleren of check-out na check-in is
  if (checkout <= checkin) {
      alert("Check-out date must be after the check-in date.");
      return;
  }


  // Voorlopig bericht
  alert(
      "Searching for available rooms..."
  );

  console.log("Check-in:", checkin);
  console.log("Check-out:", checkout);
  console.log("Guests:", occupancy);
  console.log("Rooms:", rooms);
}


function changeLanguage() {

  alert("Language selection will be added later.");
}