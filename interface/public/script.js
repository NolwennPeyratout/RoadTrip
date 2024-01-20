function planRoadTrip() {
    var country = document.getElementById("country").value;
    var travelType = document.getElementById("travelType").value;
    var situation = document.getElementById("situation").value;

    var result = "You have chosen to plan a road trip in " + country + " with a " + travelType + " travel type, and your situation is " + situation + ".";
    
    document.getElementById("result").innerText = result;
}
