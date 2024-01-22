<script setup>
// defineProps({
//   msg: {
//     type: String,
//     required: true
//   }
// })

function planRoadTrip() {
    var country = document.getElementById("country").value;
    var travelType = document.getElementById("travelType").value;
    var situation = document.getElementById("situation").value;

    var result = "You have chosen to plan a road trip in " + country + " with a " + travelType + " travel type, and your situation is " + situation + ".";
    
    //document.getElementById("result").innerText = result;
    var URI = 'http://localhost:8080/sparql?query=PREFIX act: <http://example.org/activity%23> PREFIX schema: <http://example.org/roadtrip%23> PREFIX country: <http://example.org/country%23> PREFIX transport:  <http://example.org/transport%23> SELECT ?itinerary ?startPointItName ?endPointItName ?originName ?originRating ?originAddress ?destName ?destRating ?destAddress WHERE { ?roadtrip a schema:RoadTrip; a ?type; schema:in ?country; schema:hasItinerary ?itinerary. ?itinerary schema:hasRoute ?route; schema:hasStartingPoint ?startPointIt; schema:hasEndingPoint ?endPointIt. ?route schema:hasTransport ?transport; schema:origin ?origin; schema:destination ?dest. ?startPointIt schema:hasActivityName ?startPointItName. ?endPointIt schema:hasActivityName ?endPointItName. ?origin schema:hasActivityName ?originName; OPTIONAL{?origin schema:hasRating ?originRating;} OPTIONAL{?origin schema:hasLocation [schema:hasAddress ?originAddress].} ?dest schema:hasActivityName ?destName; OPTIONAL{?dest schema:hasRating ?destRating;} OPTIONAL{?dest schema:hasLocation [schema:hasAddress ?destAddress].} ?country ?hasCountryName ?countryName. filter(?countryName="'+country+'") filter(?type=schema:'+travelType+') filter(?transport = transport:Car) }'
    console.log(URI)
    var startPoint = [];
    var endPoint = [];
    var origNames = [];
    var origRatings = [];
    var origAddresses = [];
    var destNames = [];
    var destRatings = [];
    var destAddresses = [];
    fetch(URI)
      .then(function(response) {
        return response.text()
      })
      .then(function(data) {
        var parser = new DOMParser();
        var xmlDoc = parser.parseFromString(data, 'text/xml');
        console.log(data)
        var results = xmlDoc.querySelectorAll('result');

        
        results.forEach(function(result) {
          var spartPointNameElement = result.querySelector('binding[name="startPointItName"] literal');
          
          if (spartPointNameElement) {
            var x = spartPointNameElement.textContent;
            startPoint.push(x);
          }
          var endPointNameElement = result.querySelector('binding[name="endPointItName"] literal');
          
          if (endPointNameElement) {
            var x = endPointNameElement.textContent;
            endPoint.push(x);
          }
          var origNameElement = result.querySelector('binding[name="originName"] literal');
          
          if (origNameElement) {
            var x = origNameElement.textContent;
            origNames.push(x);
          }
          var origRatingElement = result.querySelector('binding[name="originRating"] literal');
          
          if (origRatingElement) {
            var x = origRatingElement.textContent;
            origRatings.push(x);
          }
          var origAddressElement = result.querySelector('binding[name="originAddress"] literal');
          
          if (origAddressElement) {
            var x = origAddressElement.textContent;
            origAddresses.push(x);
          }
          var destNameElement = result.querySelector('binding[name="destName"] literal');
          
          if (destNameElement) {
            var x = destNameElement.textContent;
            destNames.push(x);
          }
          var destRatingElement = result.querySelector('binding[name="destRating"] literal');
          
          if (destRatingElement) {
            var x = destRatingElement.textContent;
            destRatings.push(x);
          }
          var destAddressElement = result.querySelector('binding[name="destAddress"] literal');
          
          if (destAddressElement) {
            var x = destAddressElement.textContent;
            destAddresses.push(x);
          }
          
        });
        console.log(endPoint)
        var route= "You will start from "+startPoint[0] +" rated "+origRatings[1] +" over 5 and is located at the address: "+ origAddresses[1]
        for (var i = 0; i < destAddresses.length; i++) {
          route += " and go to "+destNames[i] +" rated "+ destRatings[i]+" over 5 and is located at the address: "+ destAddresses[i]
          console.log("ici")
        }
        document.getElementById("result").innerText = route;
      })
      
    }


</script>

<template>
    <div>
  <div class="banner">
    <div class="where">
        <label for="country">Choose a Country:</label>
        <select id="country">
            <option value="United States">USA</option>
            <option value="France">France</option>
        </select>
    </div>
    <div class="howMany">
        <label for="situation">Choose Your Situation:</label>
        <select id="situation">
            <option value="individual">Individual</option>
            <option value="group">Group</option>
        </select>
    </div>
    <div class="travelType">
        <label for="travelType">Choose Travel Type:</label>
        <select id="travelType">
            <option value="RuralRoadTrip">Rural</option>
            <option value="UrbanRoadTrip">Urban</option>
        </select>
    </div>
    <div class="research"><button @click="planRoadTrip">Plan Road Trip</button></div>
  </div>
  <div id="result"></div>
</div>
  
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}
.banner{
    display: table;
    clear: both;
    float:left;
    height: 200px;
    width: 100%;
}
.where{
    float:left;
    width: 30%;
}
.research{
    float:left;
    width: 10%;
}
.travelType{
    float:left;
    width: 30%;
}
.howMany{
    float:left;
    width: 30%;
}



@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
