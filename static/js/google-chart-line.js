(function(){


google.charts.load('current', {packages: ['corechart', 'line']})

var transportId = $('#transport_id').data('transportId')
var username = $('#username').data('username')
var password = $('#password').data('password')


google.charts.setOnLoadCallback(function(){
    var charElement = new google.visualization.LineChart(
        document.getElementById('chart_div_temperatures')
    )

    refreshChart(charElement, username, password)
    setInterval(function(){
        refreshChart(charElement, username, password)
    }, 15000)
})


var tokenRequestSettings = {
    'crossDomain': true,
    'url': 'https://transports-rest-api.herokuapp.com/auth',
    'method': 'POST',
    'headers': {
      'content-type': 'application/json'
    }
}

function requestToken(username, password){
    var settings = $.extend({}, tokenRequestSettings)
    settings.data = JSON.stringify({username: username, password: password})
    return $.ajax(settings).then(function(response){
        return response.access_token
    })
}

var requestTemperaturesSettings = {
    crossDomain: true,
    url: 'https://transports-rest-api.herokuapp.com/report/' + transportId,
    method: 'GET',
    headers: {
      'content-type': 'application/json'
    }
}

function requestTemperatures(token){
    var settings = $.extend({}, requestTemperaturesSettings)
    settings.headers.authorization = 'JWT ' + token

    return $.ajax(settings).then(function(response){
        return response.reports.map(function(report){
            return report.temperature
        })
    })
}

var options = {
    hAxis: {
        title: ''
    },
    vAxis: {
        title: 'Temperatura  ºC'
    },
    animation:{
        //startup: true,
        duration: 1000,
        easing: 'out',
    },
    legend:{
        position: 'none'
    }
};


function drawBasic(chart, temperatures){
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'X');
    data.addColumn('number', 'ºC');
    data.addRows(temperatures);

    
    chart.draw(data,options);
    
    function resize(){
        var chart = new google.visualization.LineChart(document.getElementById('chart_div_temperatures'));
        chart.draw(data, options);
    }

    window.onload = resize;
    window.onresize = resize;
        
}

function refreshChart(chart, username, password){
    requestToken(username, password)
        .then(requestTemperatures)
        .then(function(temperatures){
            temperatures = temperatures.map(function(temperature, index){
                return [index, temperature]
            })
            drawBasic(chart, temperatures)
        })
}
})()