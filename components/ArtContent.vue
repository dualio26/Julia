<template>
  <div>
    <div id="AllContnet">
      <div class="pt-12 mx-auto w-10/12 block">
        <div id="Landscape" class="Landscape hidden">
          <h1 class="text-center">Landscape</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div v-for="item in lanInfo" :key="item.Piece_Title">
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
        </div>
        <div id="Hexagon" class="Hexagon hidden">
          <h1 class="text-center">Hexgon</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div v-for="item in hexInfo" :key="item.Piece_Title">
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
        </div>
        <div id="Portraits" class="Portraits hidden">
          <h1 class="text-center">Portraits</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div v-for="item in porInfo" :key="item.Piece_Title">
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
        </div>
        <div id="AllArt" class="All hidden">
          <h1 class="text-center">All My Pieces</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div v-for="item in artworks" :key="item.Piece_Title">
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
    const hexInfo = []
    const lanInfo = []
    const porInfo = []
    while (i !== len) {
      const temp = artworks[i]
      if (temp.Category === 'Hexagon') {
        hexInfo.push(temp)
      }
      if (temp.Category === 'Landscape') {
        lanInfo.push(temp)
      }
      if (temp.Category === 'Portrait') {
        porInfo.push(temp)
      }
      i++
    }
    console.log(porInfo)
    console.log(hexInfo)
    console.log(lanInfo)
    return {
      artworks,
      porInfo,
      hexInfo,
      lanInfo,
    }
  },
}
</script>
