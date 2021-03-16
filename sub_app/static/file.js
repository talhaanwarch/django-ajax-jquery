
$(document).ready(function(){
	$('#btn_submit').click(function()
	{
		console.log('button clicked')
	    var form = $('#formCreated');
	    var formdata = false;
	    if (window.FormData){
	        formdata = new FormData(form[0]);
	    }
	    var formAction = form.attr('action');
	    $.ajax({
	        url         : $("formCreated").data('url'),
	        data        : formdata ? formdata : form.serialize(),
	        cache       : false,
	        contentType : false,
	        processData : false,
	        type        : 'POST',
	        success:function(response){
				// reponse recieved from views recieved here and sent to div with resultid in home.html
				console.log(response)
				$('#resultid').append(response.text)
				// first text is key of response and second text is the text object
			
	        }
	    });
	});

})