google.charts.load('current', { 'packages': ['gauge'] })

var transportId = $('#transport_id').data('transportId')
var username = $('#username').data('username')
var password = $('#password').data('password')

google.charts.setOnLoadCallback(function () {
  var chartElement = new google.visualization.Gauge(
    document.getElementById('chart_div_current_temperature')
  )

  refreshChart(chartElement, username, password)
  setInterval(function () {
    refreshChart(chartElement, username, password)
  }, 5000)
})

var tokenRequestSettings = {
  'crossDomain': true,
  'url': 'https://transports-rest-api.herokuapp.com/auth',
  'method': 'POST',
  'headers': {
    'content-type': 'application/json'
  }
}

function requestToken(username, password) {
  var settings = $.extend({}, tokenRequestSettings)
  settings.data = JSON.stringify({ username: username, password: password })
  return $.ajax(settings).then(function (response) {
    return response.access_token
  })
}

var requestTemperatureSettings = {
  crossDomain: true,
  url: 'https://transports-rest-api.herokuapp.com/report/' + transportId,
  method: 'GET',
  headers: {
    'content-type': 'application/json'
  }
}

function refreshChart(chart, username, password) {
  requestToken(username, password)
    .then(requestTemperatures)
    .then(function (temperatures) {
      drawGauge(chart, temperatures[temperatures.length - 1])
    })
}

function requestTemperatures(token) {
  var settings = $.extend({}, requestTemperatureSettings)
  settings.headers.authorization = 'JWT ' + token

  return $.ajax(settings).then(function (response) {
    return response.reports.map(function (report) {
      return report.temperature
    })
  })
}

var chartOptions = {
  width: 500,
  height: 160,
  redFrom: 20,
  redTo: 30,
  yellowColor: '#99d6ff',
  yellowFrom: -4,
  yellowTo: 6,
  minorTicks: 10,
  min: -4,
  max: 30
}

function drawGauge(chart, temperature) {
  var data = google.visualization.arrayToDataTable([
    ['Label', 'Value'],
    ['', temperature]
  ])
  chart.draw(data, chartOptions)
}