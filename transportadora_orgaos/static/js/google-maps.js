function initMap() {
    var current_location = {lat: -15.98755379, lng: -48.0434221};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: current_location
    });
    var marker = new google.maps.Marker({
      position: current_location,
      map: map
    });
  }