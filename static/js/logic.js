// Warning isn't working when guessing repeated characters
$(function() {
	$('form').on('submit', function() {
		$.getJSON('/_processing', {
			char: $('#char').val(),
		}, function(data) {
			var lives = parseInt(data.lives)
			console.log(data.guessed_letters)
			// Win case
			if (!((data.guess_space).includes("_"))) {
				$(".row").empty();
				$("#guessed_letters").empty();
				$("#warning").empty();
				$("#lives").empty();
				$("#guess_space").empty();
				$("#message").text("You have saved the man!");
				$("#wordSplit").text("In case you forgot, your word was " + data.wordSplit + " and you survived with " + data.lives + " lives left!");
			// Alive and still playing case
			} else if (data.lives > 0) {
				$("#lives").text(data.lives);
				$("#guessed_letters").text(data.guessed_letters);
				$("#guess_space").text(data.guess_space);
				$("#warning").text(data.warning);
				// $("#space").text(data.char);
			// Dead case
			} else {
				$(".row").empty();
				$("#guessed_letters").empty();
				$("#warning").empty();
				$("#lives").empty();
				$("#guess_space").text(data.guess_space);
				$("#message").text("You have hung the man :(");
				$("#wordSplit").text("Your word was " + data.wordSplit);
			} 
			$("#char").val(''); // Clear input field
		});
		return false;
	});	
});
	
	