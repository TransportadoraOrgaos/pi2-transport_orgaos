google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);
var temperatures = $('#chart_div_temperatures').data('temperatures');
function drawBasic(){
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'X');
        data.addColumn('number', 'ºC');
    
        data.addRows(temperatures);
    
        var options = {
            hAxis: {
                title: ''
            },
            vAxis: {
                title: 'Temperatura'
            },
        };

        var chart = new google.visualization.LineChart(document.getElementById('chart_div_temperatures'));
        chart.draw(data,options);
        
        function resize(){
            var chart = new google.visualization.LineChart(document.getElementById('chart_div_temperatures'));
            chart.draw(data, options);
        }

        window.onload = resize;
        window.onresize = resize;
        
}