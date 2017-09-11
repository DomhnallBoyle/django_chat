$(document).ready(function(){
    $('#drop-down-button').click(function(){
        console.log("HELLO");
        if ($('#menu').is(':visible')) {
            $('#menu').slideUp('slow');
        }
        else {
            $('#menu').slideDown('slow');
        }
    });
});