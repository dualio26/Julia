<!-- Please remove this file from your project -->
<template>
  <div class="max-w-4xl mx-auto sm:px-6 lg:px-8 my-auto">
    <div
      class="mt-8 bg-black overflow-hidden shadow sm:rounded-lg p-6 text-white"
    >
      <h2 class="text-2xl leading-7 font-semibold text-center">
        Julia's ArtBoard
      </h2>
      <p class="mt-3 text-center">Capturing the natural beauty of NZ</p>
      <p class="mt-4 pt-4 border-t border-dashed">
        <div class="MenuButtons">
          <a @click="hideArtist()"><Button title="About Artist" /></a> <a @click="hideHexagon()"><Button title="Hexagon"/></a> <a @click="hidePortraits()"><Button title="Portraits"/></a>  
        </div>
      </p>
    </div>
    <div class="mx-auto max-w-4xl">
      <div id="AboutArtist" class="AboutArtist hidden">
        <h2 class="text-center">About Artist</h2>
      </div>
      <div id="Portraits" class="Portraits hidden">
        <h2 class="text-center">Portraits</h2>
      </div>
      <div id="Hexagon" class="Hexagon hidden">
        <h2 class="text-center ">Hexgon</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods:{
    hideArtist() {
      const x = document.getElementById("AboutArtist");
      const y = document.getElementById("Portraits");
      const z = document.getElementById("Hexagon");
      if (x.style.display === "none") {
        x.style.display = "block";
        y.style.display = "none";
        z.style.display = "none";
      } else {
        x.style.display = "none";
      }
    },
    hideHexagon() {
      const x = document.getElementById("AboutArtist");
      const y = document.getElementById("Portraits");
      const z = document.getElementById("Hexagon");
      if (z.style.display === "none") {
        x.style.display = "none";
        y.style.display = "none";
        z.style.display = "block";
      } else {
        z.style.display = "none";
      }
    },
    hidePortraits() {
      const x = document.getElementById("AboutArtist");
      const y = document.getElementById("Portraits");
      const z = document.getElementById("Hexagon");
      if (y.style.display === "none") {
        x.style.display = "none";
        y.style.display = "block";
        z.style.display = "none";
      } else {
        y.style.display = "none";
      }
    }
  }
}
</script>