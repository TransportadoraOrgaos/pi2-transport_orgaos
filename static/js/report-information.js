(function(){

    var transportId = $('#transport_id').data('transportId')
    var username = $('#username').data('username')
    var password = $('#password').data('password')


    function refresh(){
        refreshInformation(username, password)
        refreshDate(username, password)
        setInterval(function(){
            refreshInformation(username, password)
            refreshDate(username, password)
        }, 5000)
    }

    refresh()

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

    var requestReportInfoSettings = {
        crossDomain: true,
        url: 'https://transports-rest-api.herokuapp.com/report/' + transportId,
        method: 'GET',
        headers: {
          'content-type': 'application/json'
        }
    }

    function requestIsLocked(token){
        var settings = $.extend({}, requestReportInfoSettings)
        settings.headers.authorization = 'JWT ' + token

        return $.ajax(settings).then(function(response){
            return response.reports.map(function(report){
                return report.is_locked
            })
        })
    }

    function requestDate(token){
        var settings = $.extend({}, requestReportInfoSettings)
        settings.headers.authorization = 'JWT ' + token

        return $.ajax(settings).then(function(response){
            return response.reports.map(function(report){
                return report.date
                console.log(date)
            })
        })
    }

    function refreshInformation(username, password){
        requestToken(username, password)
            .then(requestIsLocked)
            .then(function(is_locked_array){
                if(is_locked_array[is_locked_array.length -1] == 1){
                    $('.is_locked').html('Fechada')
                    $('.is_locked_icon').addClass('fa fa-circle fa-module-report text-danger')
                    $('.is_locked_icon').removeClass('text-success')
                }else{
                    $('.is_locked').html('Aberta')
                    $('.is_locked_icon').addClass('fa fa-circle fa-module-report text-success')
                    $('.is_locked_icon').removeClass('text-danger')
                }
            })
    }

    function refreshDate(username, password){
        requestToken(username, password)
        .then(requestDate)
        .then(function(date_array){
            var last_date = date_array[date_array.length - 1]
            $('.report_date').html(last_date)
        })
    }
    refresh()
})()