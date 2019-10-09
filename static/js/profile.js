$(".follow-btn").click(function () {
    var username = $("#follow").data('username');
    var follow = $("#follow").attr('value') != "True";
    var csrftoken = $("#follow").data('csrf_token');

    $.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        xhr.setRequestHeader("X-CSRFToken", csrftoken);
	    }
	});
    $.ajax({
        type: "POST",
        url:  "/user/"+username+"/",
        data: { username: username , follow : follow  },
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("ERROR !!");
        }
    })
});
