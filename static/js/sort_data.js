// Sorts an array of objects by a field
function sortBy(object_to_sort, field_to_sort_by) {
    var xhttps = new XMLHttpRequest();
    xhttps.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            closed.log("s");
            var sorted = object_to_sort.order_by(field_to_sort_by);
            var output = "<div class='col-11'>";
            for (i = 0; i < sorted.length; i++) {
                output += "<p>{% question_element sorted[i] %}</p>";
            }
            output += "</div>";
            document.getElementById('sortable').firstChild = output;
        }
    }
    xhttps.send();
}