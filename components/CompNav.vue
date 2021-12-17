<template>
  <div class="MenuButtons hidden sm:grid mx-auto">
    <a @click="reload()"><Button /></a>
    <a href="/home"><Button title="About" /></a>
    <div class="dropdown">
      <a id="ArtTypes" class="Arts"><Button title="ArtWork" /></a>
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
      if (x.style.display === 'none') {
        x.style.display = 'block'
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
      if (z.style.display === 'none') {
        x.style.display = 'none'
        y.style.display = 'none'
        z.style.display = 'block'
      } else {
        z.style.display = 'none'
      }
    },
    hidePortraits() {
      const x = document.getElementById('Landscape')
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
