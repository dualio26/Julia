<template>
  <div>
    <div class="w-full mx-auto my-auto">
      <Nav />
    </div>
    <h1 class="text-2xl text-center pt-8 pb-6">Commisions</h1>
    <p class="text-center pb-12">These are peices that were completed on special request</p>
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
