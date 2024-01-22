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
    
    document.getElementById("result").innerText = result;
}

fetch('http://localhost:8080/sparql?query=select * where{ ?x ?y ?z}')
  .then(function(response) {
    return response.text()
  })
  .then(function(data) {
    var parser = new DOMParser();
    var xmlDoc = parser.parseFromString(data, 'text/xml');
    console.log(data)
    var results = xmlDoc.querySelectorAll('result');

    // Parcourir chaque résultat et traiter les données
    results.forEach(function(result) {
      // Extraire les valeurs de chaque binding
      var xElement = result.querySelector('binding[name="x"] bnode');
      var xValue = xElement ? xElement.textContent : null;

      var yElement = result.querySelector('binding[name="y"] uri');
      var yValue = yElement ? yElement.textContent : null;

      var zElement = result.querySelector('binding[name="z"] literal');
      var zValue = zElement ? zElement.textContent : null;

      // Utiliser les valeurs comme nécessaire
      console.log('x:', xValue);
      console.log('y:', yValue);
      console.log('z:', zValue);
    });
  })

// const endpointUrl = 'https://query.wikidata.org/sparql'
// const query = `
// PREFIX wd: <http://www.wikidata.org/entity/>
// PREFIX p: <http://www.wikidata.org/prop/>
// PREFIX ps: <http://www.wikidata.org/prop/statement/>
// PREFIX pq: <http://www.wikidata.org/prop/qualifier/>

// SELECT ?value WHERE {
//   wd:Q243 p:P2048 ?height.

//   ?height pq:P518 wd:Q24192182;
//     ps:P2048 ?value .
// }`

// const client = new SparqlClient({ endpointUrl })
// const stream = await client.query.select(query)

// stream.on('data', row => {
//   Object.entries(row).forEach(([key, value]) => {
//     console.log(`${key}: ${value.value} (${value.termType})`)
//   })
// })

// stream.on('error', err => {
//   console.error(err)
// })


</script>

<template>
    <div>
  <div class="banner">
    <div class="where">
        <label for="country">Choose a Country:</label>
        <select id="country">
            <option value="UnitedStates">USA</option>
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
            <option value="rural">Rural</option>
            <option value="urban">Urban</option>
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
