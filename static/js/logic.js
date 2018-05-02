$(function() {
	$('form').on('submit', function() {
		$.getJSON('/_processing', {
			char: $('#char').val(),
		}, function(data) {
			// If alive and still playing
			if (data.lives > 0) {
				$("#lives").text(data.lives);
				$("#guessed_letters").text(data.guessed_letters);
				$("#foo").text(data.guess_space);
				$("#warning").text(data.warning);
				// $("#space").text(data.char);
			// If dead
			} else if (data.lives == 0 ) {
				$(".row").empty();
				$(".guessed_letters").empty();
				$(".warning").empty();
			} else {
				console.log("We have a problem here");
			}
		});
		return false;
	});	
});
	
	