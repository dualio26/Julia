<template>
  <div
    class="sm:mt-8 w-full sm:w-8/12 mx-auto bg-black overflow-hidden shadow sm:rounded p-6 text-white"
  >
    <div class="sm:w-full mr-0">
      <h2 class="w-full text-2xl leading-7 font-semibold sm:text-center">
        Julia's ArtBoard
      </h2>
      <p class="mt-3 sm:text-center">Capturing the natural beauty of NZ</p>
    </div>

    <div class="mt-4 pt-4 border-t border-dashed">
      <div class="grid grid-cols-6 place-content-center block sm:hidden">
        <a class="mx-auto" @click="reload()"
          ><i class="fas fa-home fa-lg"></i></a
        ><i class="fas fa-user mx-auto fa-lg"></i
        ><i class="far fa-image mx-auto fa-lg"></i
        ><i class="fas fa-palette mx-auto fa-lg"></i
        ><i class="fab fa-blogger mx-auto fa-lg"></i
        ><i class="fas fa-sms mx-auto fa-lg"></i>
      </div>
      <div class="MenuButtons hidden sm:grid mx-auto">
        <a @click="reload()"><Button /></a>
        <a href="/home"><Button title="About" /></a>
        <div class="dropdown">
          <a id="ArtTypes" class="Arts" @click="ShowAll()"><Button title="ArtWork" /></a>
          <div class="dropdown-content rounded">
            <a @click="hideArtist()">Landscape</a>
            <a @click="hideHexagon()">Hexagon</a>
            <a @click="hidePortraits()">Portraits</a>
          </div>
        </div>
        <a href="/home"><Button title="Commisions" /></a>
        <a href="/home"><Button title="Blog" /></a>
        <a href="/home"><Button title="Contact" /></a>
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
    console.log(artTitles)
    document.getElementById('PortraitContent').innerHTML = artTitles
  },
  methods: {
    reload() {
      window.location.reload()
    },
    hideArtist() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      if (x.style.display === 'none') {
        console.log("INNS")
        a.style.display = 'none'
        x.style.display = 'block'
        y.style.display = 'none'
        z.style.display = 'none'
      } else {
        x.style.display = 'none'
      }
    },
    hideHexagon() {
      console.log('help')
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      if (z.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'block'
        a.style.display = 'none'
      } else {
        z.style.display = 'none'
      }
    },
    hidePortraits() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      if (y.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'block'
        z.style.display = 'none'
        a.style.display = 'none'
      } else {
        y.style.display = 'none'
      }
    },
    ShowAll() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      if (a.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
        a.style.display = 'block'
      } else {
        a.style.display = 'none'
      }
    },
  },
}
</script>