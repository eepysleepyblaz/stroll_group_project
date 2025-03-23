let poly;
let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { lat: 55.87, lng: -4.3 },
        disableDoubleClickZoom: true,
        mapTypeId: 'hybrid',
        styles: [{
            featureType: "poi",
            elementType: "labels",
            stylers: [{ visibility: "off" }],
          }]
    });
    poly = new google.maps.Polyline({
        strokeColor: "#000000",
        strokeOpacity: 1.0,
        strokeWeight: 3,
        editable: true,
    });
    poly.setMap(map);
    map.addListener("click", addLatLng);
    map.addListener("rightclick", clearPath);
}


function addLatLng( event ) {
    path = poly.getPath();
    if (path.length < 60){

        path.push(event.latLng);
        printLatLng();
    }
}

function clearPath( event ) {
    path = poly.getPath()
    if (path.length > 0){
        
        path.removeAt(path.length-1)
        printLatLng()
    }
}

function printLatLng( event ) {
    console.log("Coordinates:");
    coordString = ""
    for (let i = 0; i < poly.getPath().length; i++) {
        console.log(i+": "+poly.getPath().getAt(i).lat(), poly.getPath().getAt(i).lng());
        coordString += poly.getPath().getAt(i).lat() + "," + poly.getPath().getAt(i).lng()+":"
    }
    console.log("Path Length: "+google.maps.geometry.spherical.computeLength(poly.getPath())+"m")
    console.log("\n");

    coords = document.getElementById("coordinates")
    coords.setAttribute('value', coordString)

    lengthString = parseInt(google.maps.geometry.spherical.computeLength(poly.getPath()))
    length = document.getElementById("length")
    length.setAttribute('value', lengthString)
}

window.initMap = initMap;