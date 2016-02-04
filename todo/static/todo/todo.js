
var getTodos = function getTodos(token){
	$.get("/todo/"+ token +"/incompleted",function(data){
				console.log(data['todos']);
				var template = $('#todos-list-template').html();
				var rendered = Mustache.render(template,data);
				$('div.token_user').html(rendered);
				// add a new post 
				var template = $('#task-form-template').html();
				var rendered = Mustache.render(template);
				$('div.add_post').html(rendered);
			});
}

$(document).ready(function(){
	var template = $('#login-form-template').html();
	// context = {'test':'value'};
	// Mustache.render(template,context);
	var rendered = Mustache.render(template);
	$('div.form_class').html(rendered);


	$('#login_form').on('submit', function(event){
		event.preventDefault();
		$.post('/todo/login', $(this).serialize(), function(data){
			console.log(this);
			$('div.form_class').empty();
			$('div.token_user').text(data["user"]);
			$.cookie('token', data["user"]) 
			getTodos($.cookie('token'));

			
		});
	});
	$('.add_post').on('submit', '#task_form',function(event){
		event.preventDefault();
		var action = "/todo/"+ $.cookie('token') +"/create" ; 
		$.post(action, $(this).serialize(), function(data){
			getTodos($.cookie('token'));
		});

		
	});



	$('.token_user').on('submit', '#complete_form',function(event){
		event.preventDefault();
		var action = "/todo/"+ $.cookie('token') +"/complete_todo" ; 
		$.post(action, $(this).serialize(), function(data){
			getTodos($.cookie('token'));
		});
	});

	$('.token_user').on('submit', '#update_form',function(event){
		event.preventDefault();
		var action = "/todo/"+ $.cookie('token') +"/Update_todo" ; 
		$.post(action, $(this).serialize(), function(data){
			getTodos($.cookie('token'));
		});
	});

});