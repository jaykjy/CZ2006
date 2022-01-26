"use strict";

var map = null;
var infowindow = null;
var markers = [];
var mapState = "ewaste";

var GOOGLE_MAPS_API_KEY = "AIzaSyBnZtv1xAxEgTHcme4vJTF2SBU0f06FmqQ";

var src = "https://geo.data.gov.sg/ewaste/2021/02/19/kml/ewaste.kml";

// Defaults to centre of Singapore
var defaultPosition = {
  coords: {
    latitude: 43.672278,
    longitude: -79.3745125,
  },
};

/**
 * Switches to E-Waste data after user clicks on E-waste button
 */
function eWaste() {
  src = "https://geo.data.gov.sg/ewaste/2021/02/19/kml/ewaste.kml";
  console.log("Switched to E-Waste data!");
  initMap();
  mapState = "ewaste";
}

/**
 * Switches to Cash-For-Trash data after user clicks on Cash-For-Trash button
 */
function cashForTrash() {
  src = "https://geo.data.gov.sg/cashfortrash/2019/02/27/kml/cashfortrash.kml";
  console.log("Switched to Cash-For-Trash data!");
  initMap();
  mapState = "cashfortrash";
}

/**
 * Switches to Lighting-Waste data after user clicks on Cash-For-Trash button
 */
function lightingWaste() {
  src = "https://geo.data.gov.sg/lighting/2019/10/01/kml/lighting.kml";
  console.log("Switched to Lighting-Waste data!");
  initMap();
  mapState = "lightingwaste";
}

/**
 * Switches to Second-Hand-Goods data after user clicks on Cash-For-Trash button
 */
function secondHandGoods() {
  src =
    "https://geo.data.gov.sg/secondhandcollecn/2017/11/30/kml/secondhandcollecn.kml";
  console.log("Switched to Second Hand Goods data!");
  initMap();
  mapState = "secondhandgoods";
}

/**
 * Initialises Google Maps to user's location and displays all recycling pins
 */
function initMap() {
  // Get user's location
  var x = navigator.geolocation;
  x.getCurrentPosition(success, failure);

  // Parses the user's latitude and longitude into Google Maps
  function success(position) {
    console.log("Loaded Successfully!");

    var userLat = position.coords.latitude;
    var userLong = position.coords.longitude;

    var coords = new google.maps.LatLng(userLat, userLong);

    var mapOptions = {
      zoom: 14,
      center: coords,
    };

    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    // Add user's location as a marker
    const image =
      "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
    const userMarker = new google.maps.Marker({
      position: { lat: userLat, lng: userLong },
      map,
      icon: image,
    });

    // Adds all the markers from data.gov
    var kmlLayer = new google.maps.KmlLayer(src, {
      suppressInfoWindows: false,
      preserveViewport: true,
      map: map,
    });

    // Allows all the pins to listen for user's click
    kmlLayer.addListener("click", function (kmlEvent) {
      // Access the description of each marker
      var text = kmlEvent.featureData.description;

      // Tags to be queried
      const BUILDING = "<th>ADDRESSBUILDINGNAME</th>";
      const BLOCK = "<th>ADDRESSBLOCKHOUSENUMBER</th>";
      const STREET = "<th>ADDRESSSTREETNAME</th>";
      const POSTAL = "<th>ADDRESSPOSTALCODE</th>";
      const UNIT = "<th>ADDRESSUNITNUMBER</th>";

      // Index of Location Name
      var startIndex;
      var endIndex;
      var location;

      // Obtain pin's location
      if (mapState.localeCompare("ewaste") == 0) {
        startIndex = text.search(BUILDING);
        endIndex = text.search(BLOCK);
        location = text.slice(startIndex + 33, endIndex - 27);
      } else if (mapState.localeCompare("cashfortrash") == 0) {
        startIndex = text.search(STREET);
        endIndex = text.search(POSTAL);
        location = text.slice(startIndex + 31, endIndex - 27);
      } else if (mapState.localeCompare("lightingwaste") == 0) {
        startIndex = text.search(BUILDING);
        endIndex = text.search(UNIT);
        location = text.slice(startIndex + 33, endIndex - 27);
      } else if (mapState.localeCompare("secondhandgoods") == 0) {
        startIndex = text.search(STREET);
        endIndex = text.search(POSTAL);
        location = text.slice(startIndex + 31, endIndex - 27);
      } else {
        location = "";
        console.log("Error getting location of marker!");
      }

      // Shows the Current Selection on the page
      console.log(location);
      updateSelectedLocation(location);
      // Saves the location selected
      localStorage.setItem("location", location)
    });
  }

  // If map fails to load
  function failure() {
    console.log("Failed to load!");
  }
}

/**
 * Updates location text to be the selected Location
 * @param {string} location 
 */
function updateSelectedLocation(location) {
  document.getElementById('recycle').getElementsByTagName('p')[0].innerHTML = location;
}
