// import "http://code.jquery.com/color/jquery.color-2.1.2.js";

$('#New').click(function() {
    $('.modal').addClass('modal-show');
    $('.modal-content').addClass('modal-content-drop');
});

$('#Cancel').click(function() {
    $('.modal').removeClass('modal-show');
    $('.modal-content').removeClass('modal-content-drop');
});

$('.modal button').hover(
    function() {
        $(this).animate({
            'background-position-x': "0%",
            color: "#ffffff"
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
