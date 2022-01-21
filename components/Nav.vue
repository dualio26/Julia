<template>
  <div class="w-full bg-black overflow-hidden shadow p-6 text-white">
    <div class="w-full mr-0">
      <h2 class="w-full text-2xl leading-7 font-semibold sm:text-center">
        Julia's ArtBoard
      </h2>
      <p class="mt-3 sm:text-center">Capturing the natural beauty of NZ</p>
    </div>

    <div class="mt-4 pt-4 border-t border-dashed">
      <div class="grid grid-cols-6 place-content-center block sm:hidden">
        <a class="mx-auto" @click="hideHome()"
          ><i class="fas fa-home fa-lg"></i></a
        ><i class="far fa-image mx-auto fa-lg"></i
        ><i class="fas fa-palette mx-auto fa-lg"></i
        ><i class="fab fa-blogger mx-auto fa-lg"></i
        ><i class="fas fa-sms mx-auto fa-lg"></i>
      </div>
      <div class="MenuButtons hidden sm:grid mx-auto">
        <a @click="hideHome()"><Button /></a>
        <div class="dropdown">
          <a id="ArtTypes" class="Arts" @click="ShowAll()"
            ><Button title="ArtWork"
          /></a>
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
    let artTitles = ''
    let hexInfo = ''
    let lanInfo = ''
    let porInfo = ''
    let i = 0
    const len = data.length
    while (i !== len) {
      const temp = artworks[i]
      const tempAllInfo = `<div href="#${i}" class="Peice rounded p-3 my-auto" style="height: fit-content; max-width: fit-content;"><img src="../assets/images/${temp.Piece_Title}.jpg" alt="Art image" class="rounded m-auto" /><div class="Artinfo pt-4 hidden"><h1>${temp.Piece_Title}</h1><p>${temp.Blurb}</p><p>${temp.Dimensions} mm</p><p>${temp.Price}</p></div></div> `
      artTitles = artTitles + tempAllInfo
      if (temp.Category === 'Hexagon') {
        const temphexInfo = `<a href="#${i}" class="Peice rounded p-3 my-auto" style="height: fit-content; max-width: fit-content;"><img src="../assets/images/${temp.Piece_Title}.jpg" alt="Art image" class="rounded m-auto" /><div class="Artinfo pt-4 hidden"><h1>${temp.Piece_Title}</h1><p>${temp.Blurb}</p><p>${temp.Dimensions} mm</p><p>${temp.Price}</p></div></a> `
        hexInfo = hexInfo + temphexInfo
      }
      if (temp.Category === 'Landscape') {
        const templanInfo = `<a href="#${i}" class="Peice rounded p-3 my-auto" style="height: fit-content; max-width: fit-content;"><img src="../assets/images/${temp.Piece_Title}.jpg" alt="Art image" class="rounded m-auto" /><div class="Artinfo pt-4 hidden"><h1>${temp.Piece_Title}</h1><p>${temp.Blurb}</p><p>${temp.Dimensions} mm</p><p>${temp.Price}</p></div></a> `
        lanInfo = lanInfo + templanInfo
      }
      if (temp.Category === 'Portrait') {
        const tempporInfo = `<a href="#${i}" class="Peice rounded p-3 my-auto" style="height: fit-content; max-width: fit-content;"><img src="../assets/images/${temp.Piece_Title}.jpg" alt="Art image" class="rounded m-auto" /><div class="Artinfo pt-4 hidden"><h1>${temp.Piece_Title}</h1><p>${temp.Blurb}</p><p>${temp.Dimensions} mm</p><p>${temp.Price}</p></div></a> `
        porInfo = porInfo + tempporInfo
      }
      i++
    }
    console.log(artTitles)
    console.log(hexInfo)
    console.log(lanInfo)
    console.log(porInfo)
    document.getElementById('AllContent').innerHTML = artTitles
    document.getElementById('HexagonContent').innerHTML = hexInfo
    document.getElementById('LandscapeContent').innerHTML = lanInfo
    document.getElementById('PortraitContent').innerHTML = porInfo
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
      const b = document.getElementById('HomeContent')
      if (x.style.display === 'none') {
        b.style.display = 'none'
        a.style.display = 'none'
        x.style.display = 'block'
        y.style.display = 'none'
        z.style.display = 'none'
      } else {
        x.style.display = 'none'
      }
    },
    hideHome() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      const b = document.getElementById('HomeContent')
      if (b.style.display === 'none') {
        b.style.display = 'grid'
        a.style.display = 'none'
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
      } else {
        x.style.display = 'none'
      }
    },
    hideHexagon() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      const b = document.getElementById('HomeContent')
      if (z.style.display === 'none') {
        b.style.display = 'none'
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
      const b = document.getElementById('HomeContent')
      if (y.style.display === 'none') {
        b.style.display = 'none'
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
      const b = document.getElementById('HomeContent')
      if (a.style.display === 'none') {
        b.style.display = 'none'
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
