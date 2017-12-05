/* global google, $, transportApi */

function initMap () {
  var latitudes = $('#map').data('latitudes')
  var longitudes = $('#map').data('longitudes')
  var transportId = $('#transport_id').data('transportId')
  var el = document.getElementById('map')

  var liveRoute = createLiveRoute(el, latitudes, longitudes)

  setInterval(function () {
    transportApi.getCoords(transportId)
    .then(function (coords) {
      liveRoute.update(last(coords))
    })
  }, 5000)
}

var LiveRoute = function (marker, path) {
  this.marker = marker
  this.path = path
}

LiveRoute.prototype.update = function (coord) {
  coord = new google.maps.LatLng(coord)
  this.path.push(coord)
  this.marker.setPosition(coord)
}

var createLiveRoute = function (element, latitudes, longitudes) {
  var startPosition = { lat: latitudes[0], lng: longitudes[0] }
  var currentPosition = { lat: last(latitudes), lng: last(longitudes) }
  var coordinates = latitudes.map(function (lat, i) {
    return { lat: lat, lng: longitudes[i] }
  })

  var map = new google.maps.Map(element, {
    zoom: 12,
    center: {
      lat: (min(latitudes) + max(latitudes)) / 2,
      lng: (min(longitudes) + max(longitudes)) / 2
    }
  })
  map.addListener('click', hideAllInfos)

  createMarker(
    map, startPosition, 'Ponto de Partida', {
      url: 'http://maps.google.com/mapfiles/kml/paddle/red-circle.png',
      scaledSize: new google.maps.Size(40, 40)
    }
  )

  var marker = createMarker(
    map, currentPosition, 'Última localização', {
      url: 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png',
      anchor: new google.maps.Point(15, 15)
    }
  )

  var polyLine = new google.maps.Polyline({
    strokeColor: '#00b3fd',
    strokeOpacity: 1.0,
    strokeWeight: 6,
    map: map,
    path: coordinates
  })

  return new LiveRoute(marker, polyLine.getPath())
}

var infos = []
function hideAllInfos () {
  infos.forEach(function (i) {
    i.close()
  })
}

var createMarker = function (map, position, content, icon) {
  var info = new google.maps.InfoWindow({
    content: content
  })
  infos.push(info)

  var marker = new google.maps.Marker({
    position: position,
    map: map,
    icon: icon
  })

  marker.addListener('click', function () {
    hideAllInfos()
    info.open(map, marker)
  })

  return marker
}

function max (arr) {
  return Math.max.apply(null, arr)
}

function min (arr) {
  return Math.min.apply(null, arr)
}

function last (arr) {
  return arr[arr.length - 1]
}
