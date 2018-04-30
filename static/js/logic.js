$(function() {
	$('form').on('submit', function() {
		$.getJSON('/_processing', {
			char: $('#char').val(),
		}, function(data) {
			$("#lives").text(data.lives);
			$("#guessed_letters").text(data.guessed_letters);
			$("#foo").text(data.guess_space);
			$("#warning").text(data.warning);
			// $("#space").text(data.char);
			});
		return false;
	});	
});
	
	