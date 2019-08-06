$(document).ready(function() {

    //Summons the modal view for creating new beer entry
    $('#New').click(function() {
        $('.modal').addClass('modal-show');
        $('.modal-center').addClass('modal-center-drop');
    });
    
    //Hides the modal view
    $('#cancel').click(function() {
        $('.modal').removeClass('modal-show');
        $('.modal-center').removeClass('modal-center-drop');
    });
    
});

