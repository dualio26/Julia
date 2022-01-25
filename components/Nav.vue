<template>
  <div class="w-full bg-black overflow-hidden shadow p-6 text-white">
    <div class="w-full mr-0">
      <h2 class="w-full text-2xl leading-7 font-semibold sm:text-center">
        Julia's ArtBoard
      </h2>
      <p class="mt-3 sm:text-center">Capturing the natural beauty of NZ</p>
    </div>

    <div class="mt-4 pt-4 border-t border-dashed">
      <div class="grid grid-cols-5 place-content-center block sm:hidden">
        <a class="mx-auto" @click="hideHome()"
          ><i class="fas fa-home fa-lg"></i></a
        ><i
          class="far fa-image mx-auto fa-lg h-fit my-auto"
          @click="ShowPhoneAll()"
        ></i
        ><i href="/commisions" class="fas fa-palette mx-auto fa-lg h-fit my-auto"></i
        ><i href="/blog" class="fab fa-blogger mx-auto fa-lg h-fit my-auto"></i
        ><i href="/contact" class="fas fa-phone mx-auto fa-lg h-fit my-auto"></i>
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
        <a href="/commisions"><Button title="Commisions" /></a>
        <a href="/blog"><Button title="Blog" /></a>
        <a href="/contact"><Button title="Contact" /></a>
      </div>
    </div>
    <div id="PhoneArtNav" class="pt-8 block hidden sm:hidden">
      <div class="grid grid-cols-3">
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
export default {
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
        a.style.display = 'block'
      }
    },
    hideHome() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      const b = document.getElementById('HomeContent')
      const c = document.getElementById('PhoneArtNav')
      if (b.style.display === 'none') {
        b.style.display = 'grid'
        a.style.display = 'none'
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
        c.style.display = 'none'
      } else {
        x.style.display = 'none'
        a.style.display = 'block'
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
        a.style.display = 'block'
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
        a.style.display = 'block'
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
        b.style.display = 'block'
      }
    },
    ShowPhoneAll() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      const b = document.getElementById('HomeContent')
      const c = document.getElementById('PhoneArtNav')
      if (a.style.display === 'none') {
        b.style.display = 'none'
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
        a.style.display = 'block'
        c.style.display = 'block'
      } else {
        a.style.display = 'none'
        b.style.display = 'block'
      }
    },
  },
}
</script>
