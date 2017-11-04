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

    //START LOCATION
    var iconStart = {
        url: "http://maps.google.com/mapfiles/kml/paddle/red-circle.png",
        scaledSize: new google.maps.Size(40, 40)
    }
    var markerStart = new google.maps.Marker({
        position: start_location,
        map: map,
        icon: iconStart
    })
    var startInfo = new google.maps.InfoWindow({
        content: '<strong>Ponto de Partida</strong>'
    })
    markerStart.addListener('click', function(){
        startInfo.open(map, markerStart),
        currentLocationInfo.close(map, markerCurrentLocation)
    })

    //CURRENT LOCATION
    var iconCurrentLocation = {
        url: "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png",
        anchor: new google.maps.Point(15, 15)
    }
    var markerCurrentLocation = new google.maps.Marker({
        position: current_location,
        map: map,
        icon: iconCurrentLocation
    })
    var currentLocationInfo = new google.maps.InfoWindow({
        content: '<strong>Última Localização</strong>',
        position: current_location,
        pixelOffset: new google.maps.Size(0, 20)
    })
    markerCurrentLocation.addListener('click', function(){
        currentLocationInfo.open(map, markerCurrentLocation),
        startInfo.close(map,startInfo)
    })

    //Listen for click on map
    google.maps.event.addListener(map,'click', function(event){
        currentLocationInfo.close(map, markerCurrentLocation)
        startInfo.close(map,startInfo)
    })
    
}