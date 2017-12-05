$(document).ready(function() {

    var username = $('#username').data('username')
    var password = $('#password').data('password')
    window.transportApi = new TransportAPI(username, password)

    var errorMessage = $('#error_message').data('errorMessage')

    if (errorMessage){
        $('#cadastro_camara').modal({
            show: true,
            backdrop: 'static',
            keyboard: false
        });
    }else{
        $('#cadastro_camara').modal({
            show: false,
            backdrop: 'static'
        });
        $('.delete-camara').modal({
            show: false,
            backdrop: 'static'
        });
    }
});