/* global $  */
var tokenRequestSettings = {
  'crossDomain': true,
  'url': 'https://transports-rest-api.herokuapp.com/auth',
  'method': 'POST',
  'headers': {
    'content-type': 'application/json'
  }
}

var reportSettings = {
  crossDomain: true,
  url: 'https://transports-rest-api.herokuapp.com/report/',
  method: 'GET',
  headers: {
    'content-type': 'application/json'
  }
}

var TransportAPI = function (username, password) {
  this.username = username
  this.password = password
}

TransportAPI.prototype.requestToken = function () {
  var settings = $.extend({}, tokenRequestSettings)
  settings.data = JSON.stringify({
    username: this.username,
    password: this.password
  })
  return $.ajax(settings).then(function (response) {
    return response.access_token
  })
}

TransportAPI.prototype.requestReports = function (transportId) {
  return this.requestToken()
  .then(function (token) {
    var settings = $.extend({}, reportSettings)
    settings.headers.authorization = 'JWT ' + token
    settings.url = settings.url + transportId
    return $.ajax(settings)
  })
}

TransportAPI.prototype.getTemperatures = function (transportId) {
  return this.requestReports(transportId)
  .then(function (response) {
    return response.reports.map(function (report) {
      return report.temperature
    })
  })
}

TransportAPI.prototype.getCoords = function (transportId) {
  return this.requestReports(transportId)
  .then(function (response) {
    return response.reports.map(function (report) {
      return { lat: report.latitude, lng: report.longitude }
    })
  })
}
