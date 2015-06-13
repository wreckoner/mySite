var map;
var marker;

function trendSelect(source) {
	// body...
	$(".trend").hide();
	$(source).fadeIn();
}

function initialize() {
	// Initialize function to initialize google map
	var mapOptions = {
	center:new google.maps.LatLng(0, 0),
	zoom:2,
	mapTypeId:google.maps.MapTypeId.TERRAIN
	};
	map=new google.maps.Map(document.getElementById("googleMap"),mapOptions);

	// This event listener will call addMarker() when the map is clicked.
	google.maps.event.addListener(map, 'click', function(event) {
	addMarker(event.latLng);
	});
}

// Clear any existing marker and add a new marker to the map at the clicked location.
// Also updates the values of the text inputs to current latitude and longitude
function addMarker(location) {
	if (marker){
		marker.setMap(null);
	}
  	marker = new google.maps.Marker({
    	position: location,
    	// animation:google.maps.Animation.BOUNCE,
    	map: map
  	});
  	var infoWindow = new google.maps.InfoWindow({
  		content : 'Latitude: '+location.lat()+'<br>Longitude: '+location.lng()
  	});
  	infoWindow.open(map, marker);
  	$("#lat").val(location.lat());
  	$("#lng").val(location.lng());
}

function loadScript() {
	var script = document.createElement("script");
	script.src = "http://maps.googleapis.com/maps/api/js?callback=initialize";
	document.body.appendChild(script);
}

//Called on clicking the where on earth button. sends a query to yahoo place finder to get details for the lat and long.
function whereOnEarth () {
	var lat = $("#lat").val()
	var lng = $("#lng").val()
	if ( !isNumber(lat) || !isNumber(lng)){ $("#twitter-location-alert").fadeIn();}
	else {
		$("#twitter-location-alert").fadeOut();

		$.get("http://query.yahooapis.com/v1/public/yql", {q : 'select * from geo.placefinder where text="'+lat+','+lng+'" and gflags="R"'})
		.done(function(data){
			$xml = $(data);
			$("#twitter-postal").text($xml.find("postal").text());
			$("#twitter-neighborhood").text($xml.find("neighborhood").text());
			$("#twitter-city").text($xml.find("city").text());
			$("#twitter-county").text($xml.find("county").text());
			$("#twitter-state").text($xml.find("state").text());
			$("#twitter-country").text($xml.find("country").text());
			$("#twitter-woeid").text($xml.find("woeid").text());
		})
	}
}

function isNumber(n) {
	// Checks if n is a number. Could be a string or anything, as long as its a number! STACKOVERFLOW!
  return !isNaN(parseFloat(n)) && isFinite(n);
}