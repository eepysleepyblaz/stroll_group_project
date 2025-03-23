let poly;
let map;
// based off of google maps API website example code
const data = JSON.parse(document.getElementById('coords').textContent);
if (data != null){
    lines = data.split(":");
    coords = [];
    for (let i = 0; i < lines.length-1; i++){
        x = lines[i].split(",")
        coords[i] = {lat: parseFloat(x[0]), lng: parseFloat(x[1])};
    }
}
else coords = []

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: (coords.length > 0 ? coords[0] : {lat: 55.8617, lng: -4.2583}),
        mapTypeId: 'hybrid',
        styles: [{
            featureType: "poi",
            elementType: "labels",
            stylers: [{ visibility: "off" }],
          }]
    });
    poly = new google.maps.Polyline({
        path: coords,
        strokeColor: "#000000",
        strokeOpacity: 1.0,
        strokeWeight: 3,
        editable: false,
    });
    poly.setMap(map);
}

window.initMap = initMap;
