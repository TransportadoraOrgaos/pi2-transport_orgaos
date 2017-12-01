$(document).ready(function() {

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