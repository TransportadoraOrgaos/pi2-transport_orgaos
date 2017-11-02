google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(drawChart);

var currentTemperature = $('#chart_div_current_temperature').data('currentTemperature');

function drawChart() {

  var data = google.visualization.arrayToDataTable([
    ['Label', 'Value'],
    ['', Number(currentTemperature)]
  ]);

  var options = {
    width: 500, height: 160,
    redFrom: 0, redTo: 4,
    yellowColor: "#99d6ff", yellowFrom:-4, yellowTo: 0,
    minorTicks: 10,
    min: -4,
    max: 4
  };

  var chart = new google.visualization.Gauge(document.getElementById('chart_div_current_temperature'));     
  chart.draw(data, options);
}