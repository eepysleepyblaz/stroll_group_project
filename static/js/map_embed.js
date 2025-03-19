let poly;
let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { lat: 55.87, lng: -4.3 },
    });
    poly = new google.maps.Polyline({
        strokeColor: "#000000",
        strokeOpacity: 1.0,
        strokeWeight: 3,
        editable: true,
    });
    poly.setMap(map);
    map.addListener("click", addLatLng);
}



function addLatLng(event) {
    const path = poly.getPath();

    path.push(event.latLng);
    printLatLng();
}

function printLatLng( event ) {
    console.log("Coordinates:");
    for (let i = 0; i < poly.getPath().length; i++) {
        console.log(i+": "+poly.getPath().getAt(i).lat(), poly.getPath().getAt(i).lng());
        }
    console.log("Path Length: "+google.maps.geometry.spherical.computeLength(poly.getPath()))
    console.log("\n");
}

window.initMap = initMap;