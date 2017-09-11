$(document).ready(function(){
   reload();
});

function reload() {
    $('.room-list-item-info-wrapper').click(function(){
        var room_name = $(this).children('.room-label').text().trim();
        var data = {
            'room_name': room_name
        };
        location.href = "/room/?room_name=" + room_name;
    });

    $('#create-room-button').click(function(){
        var room_name_input = $('#create-room-name')
        var room_name = room_name_input.val();
        if (room_name.length == 0) {
            alert('Please enter a Chatroom name.');
            room_name_input.css('border', '1px solid red');
            return;
        }

        var users = [];
        $('.user-checkbox input').each(function() {
            if (this.checked) {
                users.push(this.name);
            }
        });

        var data = {
            'room_name': room_name,
            'users': users
        };
        var success = function(data) {
            alert('Chatroom created successfully.');
            $('#room-list').html(data);
            reload();
        };
        make_request('/create_room/', 'POST', data, {}, success, null);
    });

    $('.delete-room i').click(function() {
        var data = {
            'room_name': $(this).data('name')
        };

        var success = function(data) {
            alert('Chatroom deleted successfully.');
            $('#room-list').html(data);
        };
        make_request('/delete_room/', 'POST', data, {}, success, null);
    });

    $('.edit-room i').click(function() {
        var room_name = $(this).data('name');
        var creator = $(this).data('creator');
        var members = $(this).data('members').split(',');
        members.pop();

        $("#dialog-box").dialog({
            title: 'Edit Chatroom',
            modal: true,
            draggable: false,
            resizable: false,
            show: 'blind',
            hide: 'blind',
            width: 400,
            dialogClass: 'edit-chatroom',
            open: function () {
                var members_html = '<ul id="members">';
                for ($i=0; $i<members.length; $i++) {
                    members_html += '<li>' + members[$i] +
                    '<button><i class="material-icons">clear</i></button></li>';
                }
                members_html += '</ul>';

                $(this).html('Chatroom:<input id="room_name" value="' + room_name + '"/>' +
                    '<br>Admin:<input id="admin" value="' + creator + '"/>' +
                    '<br>Members:<div>' + members_html + '</div>' +
                    '<br>Add Members:<div><input id="add-member" placeholder="Name"/><button id="add">Add</button></div>'
                );
                $("#members li button").click(function() {
                    $(this).parent()[0].remove();
                });
                $('#admin').autocomplete({
                    source: "/user/",
                    minLength: 3,
                });
                $('#add-member').autocomplete({
                    source: "/user/",
                    minLength: 3,
                });
                $('#add').click(function(){
                    var username = $('#add-member').val();
                    if (username != '') {
                        var found = false;
                        $('#members li').each(function(idx){
                            var search_text = $(this)[0].innerText;
                            if (search_text.indexOf(username) != -1) {
                                alert("User already in group.");
                                found = true;
                                return false;
                            }
                        });
                        if (!found) {
                            $('#members').append('<li>' + username +
                                '<button><i class="material-icons">clear</i></button></li>'
                            );
                            $("#members li button").click(function() {
                                $(this).parent()[0].remove();
                            });
                        }
                        $('#add-member').val('');
                    }
                    else {
                        alert('Please enter a user.')
                    }
                });
            },
            buttons: {
                "Save": function() {
                    var new_room_name = $('#room_name').val();
                    var admin = $('#admin').val();
                    var members = [];

                    if (new_room_name == '' || admin == '') {
                        alert('Room name and admin cannot be empty');
                        return;
                    }

                    $('#members li').each(function() {
                        members.push($(this).text().replace('clear', ''));
                    });

                    var data = {
                        'old_room_name': room_name,
                        'new_room_name': new_room_name,
                        'admin': admin,
                        'members': members
                    };
                    var success = function(data) {
                        alert("Room successfully updated.");
                        $('#dialog-box').dialog('close');
                        $('#room-list').html(data);
                    };

                    make_request('/edit_room/', 'POST', data, {}, success, null);
                }
            }
        });
    });
}