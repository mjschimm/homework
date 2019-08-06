$(document).ready(function() {

    $('.form-button').hover(
        function() {
            $(this).animate({
                'background-position-x': "0%",
                color: "#fff"
            }, {
                duration: 250,
                queue: false
            });
        }, function() {
            $(this).animate({
                'background-position-x': "99%",
                'color': '#666'
            }, {
                duration: 250,
                queue: false
            });
        }
    );

});