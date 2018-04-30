$(function() {
	$('form').on('submit', function() {
		console.log('hi');
		$.getJSON('/_processing', {
			world: $('#world').val(),
		}, function(data) {
			$("#lives").text(data.lives);
			$("#guessed_letters").text(data.guessed_letters);
			$("#guess_space").text(data.guess_space);
			$("#warning").text(data.warning);
			});
		return false;
	});	
});
	
	
		
	

// $(function() {
//  	$('#char').bind('keydown', function(e) {
//  		if(e.keyCode==13)
//  		$.getJSON('/_process', {
//  			char: $('input[name="char"]').val(),
//  		}, function(data) {
 			// $("#lives").text(data.lives);
 			// $("#guessed_letters").text(data.guessed_letters);
 			// $("#guess_space").text(data.guess_space);
 			// $("#warning").text(data.warning);
//  		});
//  		return false
//  	});
// });


// $(function() {
// 	$('#level').bind('keydown', function(e) {
// 		var level = $('#level').serialize();
// 		$.post({
// 			url:'/',
// 			// data: $('#level').serialize(),
// 			data: level,
// 			type: 'POST',
// 			success: function(response) {
// 				console.log(response);
// 			},
// 			error: function(error) {
// 				console.log(error);
// 			}
// 		});
// 	});
// 	event.preventDefault();
// });

// document.getElementById('level').addEventListener('keydown', function(e) {
// 	var value = document.getElementById('level').value;
// 	if (e.code == 'Enter' && value) {
// 		.post("/easy", value, funtion(){});
// 	event.preventDefault
// 	}
// }
// level = "easy"
