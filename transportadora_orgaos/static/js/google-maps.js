function initMap() {

    var latitude = $("#map").data("latitude");
    var longitude = $("#map").data("longitude");

    console.log("Latitude: " + latitude);
    console.log("Longitude: " + longitude);

    var current_location = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: current_location
    });
    var marker = new google.maps.Marker({
      position: current_location,
      map: map
    });
  }