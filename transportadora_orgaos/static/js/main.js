$(document).ready(function() {

    var errorMessage = $('#error_message').data('errorMessage')

    if (errorMessage){
        console.log(errorMessage)
        $('#cadastro_camara').modal({
            show: true,
            backdrop: 'static',
            keyboard: false
        });
    }else{
        console.log('sem errorMessage')
        $('#cadastro_camara').modal({
            show: false,
            backdrop: 'static'
        });
    }
});