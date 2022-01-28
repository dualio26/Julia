<template>
  <div>
    <div class="w-full mx-auto my-auto">
      <Nav />
    </div>
    <div v-for="item in TheInfo" :key="item.Piece_Title">
      <!-- file information is loaded but need to add /assets/images/ to the src -->
      <div
        class="Peice rounded p-3 mx-auto my-4 sm:my-0"
        style="height: fit-content"
      >
        <img
          :src="`/Artwork/${item.Piece_Title}.jpg`"
          alt="Art image"
          class="rounded"
        />
        <div class="Artinfo pt-4 hidden">
          <h1>{{ item.Piece_Title }}</h1>
          <p>${{ item.Blurb }}</p>
          <p>{{ item.Dimensions }} mm</p>
          <p>{{ item.Price }}</p>
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
    const len = data.length
    let i = 0
    const TheInfo = []
    while (i !== len) {
      const temp = artworks[i]
      if (temp.Category === 'Commision') {
        TheInfo.push(temp)
      }
      i++
    }
    return {
      TheInfo,
    }
  },
}
</script>
