<template>
  <div id="AllContnet">
    <div class="pt-12 mx-auto w-10/12 block">
      <div id="Landscape" class="Landscape hidden">
        <h1 class="text-center">Landscape</h1>
        <div id="LandscapeContent" class="hidden"></div>
      </div>
      <div id="Hexagon" class="Hexagon hidden">
        <h1 class="text-center">Hexgon</h1>
        <p id="HexagonContent" class="hidden sm:flex flex-wrap gap-4"></p>
      </div>
      <div id="Portraits" class="Portraits hidden">
        <h1 class="text-center">Portraits</h1>
        <p id="PortraitContent" class="hidden sm:flex flex-wrap gap-4"></p>
      </div>
      <div id="AllArt" class="All hidden">
        <h1 class="text-center">All My Pieces</h1>
        <div v-for="item in artworks" :key="item.Piece_Title">
          <!-- file information is loaded but need to add /assets/images/ to the src -->
         <img :src="item.Piece_Title" alt=""/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import data from '~/content/data.json'
export default {
  data() {
    const artworks = data
    return {
    artworks
    }
  },
}
</script>
