$(document).ready(function(){
    $("#submit").click(function(){
        var dataSend = {
            "key": "1"
        }
        $.ajax({
            url: '/form/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(dataSend),
            dataType: 'json',
            processData: false,
            success: function (data) {
              console.log(data);
              window.location('predict.html');
            }
        });
    });
});