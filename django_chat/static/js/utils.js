function make_request(url, type, data, headers, success, error){
    if (type == 'POST'){
        headers['X-CSRFToken'] = Cookies.get('csrftoken');
    }
    $.ajax({
        url: url,
        type: type,
        headers: headers,
        data: data,
        success: function(data){
            success(data);
        },
        error: function(xhr){
            alert(xhr.responseText);
            if (error != null) {
                error(xhr);
            }
        },
    });
}