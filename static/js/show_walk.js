let poly;
let map;

const data = JSON.parse(document.getElementById('coords').textContent);
lines = data.split(":");
coords = [];
for (let i = 0; i < lines.length-1; i++){
    x = lines[i].split(",")
    coords[i] = {lat: parseFloat(x[0]), lng: parseFloat(x[1])};
}

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { lat: 55.87, lng: -4.3 },
    });
    poly = new google.maps.Polyline({
        path: coords,
        strokeColor: "#000000",
        strokeOpacity: 1.0,
        strokeWeight: 3,
        editable: true,
    });
    poly.setMap(map);
}

window.initMap = initMap;
