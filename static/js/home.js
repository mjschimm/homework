$('.delete').click(function() {
    alert(this.value);
    data = this.value;
    $.post("", function( data ) {
        // $( ".result" ).html( data );
    });
});