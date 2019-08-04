$('#New').click(function() {
    // alert("fuck")
    // console.log($(this));
    $('.modal').addClass('modal-show');
    $('.modal-content').addClass('modal-content-drop');
});

$('#Cancel').click(function() {
    // alert("fuck")
    // console.log($(this));
    $('.modal').removeClass('modal-show');
    $('.modal-content').removeClass('modal-content-drop');
});