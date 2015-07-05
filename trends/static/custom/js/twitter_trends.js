var map;			// Google map variable
var marker;			// User clicked marker
var woeid = {};		// WOEID clicked by user
var markers = [];	// Array of secondary markers

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
		// clear main marker if it exists.
		marker.setMap(null);
	}
	clearSecondaryMarkers();
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

function whereOnEarth () {
	//Called on clicking the where on earth button. sends a query to yahoo place finder to get details for the lat and long.
	var lat = $("#lat").val()
	var lng = $("#lng").val()
	if ( !isNumber(lat) || !isNumber(lng)){ $("#twitter-location-alert").fadeIn();}
	else {
		$("#twitter-location-alert").fadeOut();

		$.get("http://query.yahooapis.com/v1/public/yql", {q : 'select * from geo.placefinder where text="'+lat+','+lng+'" and gflags="R"'})
		.done(function(data){
			$xml = $(data);
			woeid.woeid = parseInt($xml.find("woeid").text());
			woeid.lat = lat;
			woeid.lng = lng;
			$("#twitter-postal").text($xml.find("postal").text());
			$("#twitter-neighborhood").text($xml.find("neighborhood").text());
			$("#twitter-city").text($xml.find("city").text());
			$("#twitter-county").text($xml.find("county").text());
			$("#twitter-state").text($xml.find("state").text());
			$("#twitter-country").text($xml.find("country").text());
			$("#twitter-woeid").text(woeid.woeid);
			$("#btn-closest").show();
		})
	}
}

function OnClosest(){
	//Calls the backend to retrieve a list of closest woeids and marks them on the map.
	var tempMarker;
	var infoWindow;
	$.get("twitter_trends_closest", {lat : woeid.lat, lng : woeid.lng })
	.done(function(data){
		console.log(data);
	})
}

function clearPrimaryMarker(){
	// Clears the main marker
	if (marker){
		marker.setMap(null);
	}
}

function clearSecondaryMarkers(){
	// Clears all secondary markers and array
	for (var i=0; i<markers.length; i++){
		markers[i].setMap(null);
	}
	markers = [];
}

function isNumber(n) {
	// Checks if n is a number. Could be a string or anything, as long as its a number! STACKOVERFLOW!
  return !isNaN(parseFloat(n)) && isFinite(n);
}