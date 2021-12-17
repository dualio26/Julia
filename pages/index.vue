<template>
  <div>
    <Nav />
    <div class="pt-12 mx-auto w-10/12 hidden sm:block">
      <div id="AboutArtist" class="AboutArtist hidden">
        <h1 class="text-center">Landscape</h1>
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
    <div class="pt-8 block sm:hidden">
      <div class="grid grid-cols-3 gap-10 mx-auto w-2/5">
        <a class="mx-auto w-fit" @click="hideArtist()"
          ><i class="fas fa-mountain fa-2x"></i
        ></a>
        <a class="mx-auto w-fit" @click="hideHexagon()"
          ><i class="fas fa-square fa-2x"></i
        ></a>
        <a class="mx-auto w-fit" @click="hidePortraits()"
          ><i class="fas fa-portrait fa-2x"></i
        ></a>
      </div>
      <div id="AboutArtist" class="AboutArtist hidden">
        <h1 class="text-center">Landscape</h1>
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
  methods: {
    hideArtist() {
      const x = document.getElementById('AboutArtist')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      if (x.style.display === 'none') {
        x.style.display = 'block'
        y.style.display = 'none'
        z.style.display = 'none'
      } else {
        x.style.display = 'none'
      }
    },
    hideHexagon() {
      console.log('help')
      const x = document.getElementById('AboutArtist')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      if (z.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'block'
      } else {
        z.style.display = 'none'
      }
    },
    hidePortraits() {
      const x = document.getElementById('AboutArtist')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      if (y.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'block'
        z.style.display = 'none'
      } else {
        y.style.display = 'none'
      }
    },
  },
}
</script>
