function initMap() {

    var latitudes = $("#map").data("latitudes")
    var longitudes = $("#map").data("longitudes")
    var coordinates = []
    var current_location = {lat: latitudes[latitudes.length-1], lng: longitudes[longitudes.length-1]}
    var start_location = {lat: latitudes[0], lng: longitudes[0]}


    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {
            lat: (latitudes[latitudes.length-1] + latitudes[0])/2,
            lng: (longitudes[longitudes.length-1] + longitudes[0])/2
        }
    });

    for (var i = 0, j=0; i < latitudes.length; i++, j++) {
        console.log(latitudes[i], longitudes[j])
        coordinates[i] = {lat: latitudes[i], lng: longitudes[i]}
    }

    var path = new google.maps.Polyline({
        path: coordinates,
        strokeColor: '#00b3fd',
        strokeOpacity: 1.0,
        strokeWeight: 6
    })

    path.setMap(map);


    var iconStart = "http://maps.google.com/mapfiles/kml/pal5/icon13.png"
    var iconCurrentLocation = "http://maps.google.com/mapfiles/kml/pal5/icon14.png"

    var markerStart = new google.maps.Marker({
        position: start_location,
        map: map,
        icon: iconStart
    })

    var markerCurrentLocation = new google.maps.Marker({
        position: current_location,
        map: map,
        icon: iconCurrentLocation
    })
    
}