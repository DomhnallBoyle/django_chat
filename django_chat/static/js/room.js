$(document).ready(function(){
    console.log(window.location.href);

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var room_name = window.location.href.split('/')[4].split('=')[1];
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat/" + room_name);

    chatsock.onmessage = function(message) {
        console.log(message.data);
        var message = $('#compose-message-input').val();
        var logged_in_user = $('#username').text().split(':')[1].trim();
        var date_time_string = moment().format('DD/MM/YYYY hh:mm A');

        var message_html = '<div class="message">' +
                               '<div class="square square-right">' +
                                   '<div class="message-text">' +
                                        message +
                                   '</div>' +
                                   '<div class="message-info">' +
                                        logged_in_user + ' - ' + date_time_string +
                                   '</div>' +
                               '</div>' +
                               '<div class="triangle triangle-right">' +
                               '</div>' +
                           '</div>';

        $('#messages').append(message_html);
    };

    $("#compose-message-form").on("submit", function(event) {
        var message = {
            sender: $('#username').text().split(':')[1].trim(),
            message: $('#compose-message-input').val(),
        }
        console.log(message);
        chatsock.send(JSON.stringify(message));
        return false;
    });

    $('.message').each(function() {
        var message_info = $(this).find('.message-info').text().trim();
        var handle = message_info.split(' ')[0];
        var logged_in_user = $('#username').text().split(':')[1].trim();

        if (handle == logged_in_user) {
            $(this).find('.square').addClass('square-right');
            $(this).find('.triangle').addClass('triangle-right');
        }
        else {
            $(this).find('.square').addClass('square-left');
            $(this).find('.triangle').addClass('triangle-left');
        }
    });
});
