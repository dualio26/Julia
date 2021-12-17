<template>
  <div>
    <Nav />
    <div class="pt-12 mx-auto w-10/12">
      <div id="AboutArtist" class="AboutArtist hidden">
        <h1 class="text-center">About Artist</h1>
        <p id="AboutContent"></p>
      </div>
      <div id="Hexagon" class="Hexagon hidden">
        <h1 class="text-center">Hexgon</h1>
        <p id="HexagonContent"></p>
      </div>
      <div id="Portraits" class="Portraits hidden">
        <h1 class="text-center">Portraits</h1>
        <p id="PortraitContent"></p>
      </div>
    </div>
  </div>
</template>

<script>
import data from '~/content/data.json'
export default {
   mounted() {
    const artworks = data
    const artTitles = []
    let i = 0
    const len = data.length
    while (i !== len) {
      const temp = artworks[i]
      if (temp.Category === 'Hexagon') {
        artTitles.push(temp.Blurb)
        i++
      }
      i++
    }
    document.getElementById('PortraitContent').innerHTML = artTitles
  },
}
</script>
