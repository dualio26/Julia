<!-- Please remove this file from your project -->
<template>
  <div class="w-full mx-auto sm:px-6 lg:px-8 my-auto">
    <div
     class="sm:mt-8 w-full sm:w-8/12 mx-auto bg-black overflow-hidden shadow rounded p-6 text-white"
    >
      <div class="w-9/12 sm:w-full mr-0">
        <h2 class="w-full text-2xl leading-7 font-semibold sm:text-center">
          Julia's ArtBoard
        </h2>
        <p class="mt-3 sm:text-center">Capturing the natural beauty of NZ</p>
      </div>
      <div class="mt-4 pt-4 border-t border-dashed">
        <div class="MenuButtons hidden sm:grid mx-auto">
          <a @click="reload()"><Button /></a>
          <a href="/home"><Button title="About" /></a>
          <div class="dropdown">
            <a id="ArtTypes" class="Arts"
              ><Button title="ArtWork"
            /></a>
            <div class="dropdown-content rounded">
              <a @click="hideArtist()">About Artist</a>
              <a @click="hideHexagon()">Hexagon</a>
              <a @click="hidePortraits()">Portraits</a>
            </div>
          </div>
          <a href="/home"><Button title="Commisions" /></a>
          <a href="/home"><Button title="Blog" /></a>
          <a href="/home"><Button title="Contact" /></a>
        </div>
      </div>
    </div>
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
  methods: {
    reload() {
      window.location.reload()
    },
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
