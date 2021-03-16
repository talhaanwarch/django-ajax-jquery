$(document).ready(function(){

	$('#btn_submit').click(function()
	{
		var serializedData=$('#formCreated').serialize();
		// console.log(serializedData)


		$.ajax({
			url:$("formCreated").data('url'),
			data:serializedData,
			type:'POST',
			success:function(response){
				// reponse recieved from views recieved here and sent to div with resultid in home.html
				console.log(response)
				$('#resultid').append(response.text.text)
				// first text is key of response and second text is the text object
			}
		})

		$('#formCreated')[0].reset();
	});

});