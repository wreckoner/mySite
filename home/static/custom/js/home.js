function menuSelect (argument) {
	$(".jumbotron p").empty();
	$(".row").hide();
	$(".jumbotron p").text(
		function(){ 
			if (argument == ".prosearch")
				{return "Projects and Research";}
			else if(argument == ".work")
				{return "Work";}
			else if (argument == ".education")
				{return "Education";}
		}).fadeIn();
	$(argument).fadeToggle();
}