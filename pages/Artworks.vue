<template>
  <div>
    <div class="w-full mx-auto my-auto">
      <Nav />
      <div class="mx-auto hidden sm:block pt-8" style="width: fit-content">
        <a class="px-4 font-bold" @click="hideArtist()">Landscape</a>
        <a class="px-4 font-bold" @click="hideHexagon()">Hexagon</a>
        <a class="px-4 font-bold" @click="hidePortraits()">Portraits</a>
      </div>
      <div id="PhoneArtNav" class="pt-8 block sm:hidden">
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
    <ArtContent class="pb-12" />
    <Footer />
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
      if (x.style.display === 'none') {
        a.style.display = 'none'
        x.style.display = 'block'
        y.style.display = 'none'
        z.style.display = 'none'
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
      if (z.style.display === 'none') {
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
      if (y.style.display === 'none') {
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
      if (a.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
        a.style.display = 'block'
      } else {
        a.style.display = 'none'
      }
    },
    ShowPhoneAll() {
      const x = document.getElementById('Landscape')
      const y = document.getElementById('Portraits')
      const z = document.getElementById('Hexagon')
      const a = document.getElementById('AllArt')
      const c = document.getElementById('PhoneArtNav')
      if (a.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'none'
        a.style.display = 'block'
        c.style.display = 'block'
      } else {
        a.style.display = 'none'
      }
    },
  },
}
</script>

<style>
a{
        cursor: pointer;
    }
</style>