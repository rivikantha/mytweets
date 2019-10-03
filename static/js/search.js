$(document).ready(function(){

	$("#search-query").keyup(function(){

	    $("#search-form").submit(search_submit());
	});

});


/*$('#search-form').submit(function(e){

	$.post('/search/',$(this).serialize(),function(data){

		$('.tweets').html(data);
	});

	e.preventDefault();
});*/


function search_submit(){

	var query = $('#search-query').val();

	if(query != ""){

		$('.tweets').load(

			"/search/?AJAX&query=" + encodeURIComponent(query)
		);
		
	}else{

		$('.tweets').html("");

	}	

	return false;

}