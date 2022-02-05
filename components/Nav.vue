<template>
  <div class="w-full bg-black overflow-hidden shadow p-6 text-white">
    <div class="w-full mr-0">
      <h2 class="w-full text-2xl leading-7 font-semibold sm:text-center">
        Julia's ArtBoard
      </h2>
      <p class="mt-3 sm:text-center">Capturing the natural beauty of NZ</p>
    </div>

    <div class="mt-4 pt-4 border-t border-dashed">
      <div
        class="grid place-content-center gap-6 block sm:hidden"
        style="grid-template-columns: auto auto auto auto auto"
      >
        <a href="/" class="mx-auto"><i class="fas fa-home fa-lg" style="color: white;"></i></a
        ><a href="/Artworks"
          ><i class="far fa-image mx-auto fa-lg h-fit my-auto" style="color: white;"></i></a
        ><a href="/commisions" style="width: fit-content"
          ><i class="fas fa-palette mx-auto fa-lg h-fit my-auto" style="color: white;"></i></a
        ><a href="/blog" style="width: fit-content"
          ><i class="fab fa-blogger mx-auto fa-lg h-fit my-auto" style="color: white;"></i></a
        ><a href="/contact" style="width: fit-content">
          <i class="fas fa-phone mx-auto fa-lg h-fit my-auto" style="color: white;"></i
        ></a>
      </div>
      <div class="MenuButtons hidden sm:grid mx-auto">
        <a href="/"><Button /></a>
        <div class="dropdown">
          <a id="ArtTypes" href="/Artworks" class="Arts"
            ><Button title="ArtWork"
          /></a>
        </div>
        <a href="/commisions"><Button title="Commisions" /></a>
        <a href="/blog"><Button title="Blog" /></a>
        <a href="/contact"><Button title="Contact" /></a>
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
