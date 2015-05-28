function menuSelect (argument) {
	
	$(".jumbotron p").hide(
		function() {
				$(this).text(
			function(){ 
				if (argument == ".prosearch")
					{return "Projects and Research";}
				else if(argument == ".work")
					{return "Work";}
				else if (argument == ".education")
					{return "Education";}
			}).fadeIn();
		});
	$(".row").hide();
	$(argument).fadeToggle();
}