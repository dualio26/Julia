<template>
  <div>
    <div id="AllContnet">
      <div class="pt-12 mx-auto w-10/12 block">
      <p class="text-center pb-12">This page includes Peices that I have made, these include sold and unsold peices</p>
        <div id="Landscape" class="Landscape hidden">
          <h1 class="text-center pb-6">Landscape</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div
              v-for="item in lanInfo"
              :key="item.Piece_Title"
              class="my-auto"
              witch="fit-content"
            >
              <!-- file information is loaded but need to add /assets/images/ to the src -->
              <a @click="ShowContentView(item.ID)"
                ><div
                  class="Peice rounded p-3 mx-auto my-4 sm:my-0 relative"
                  style="height: fit-content"
                >
                  <img
                    :src="`/Artwork/${item.Piece_Title}.jpg`"
                    alt="Art image"
                    class="rounded relative w-full"
                  />
                  <img
                    v-if="item.Sold"
                    src="/Artwork/SoldBanner.svg"
                    alt=""
                    class="w-inherit h-inherit absolute top-0 left-0"
                    style="height: -webkit-fill-available"
                  /></div
              ></a>
            </div>
          </div>
        </div>
        <div id="Hexagon" class="Hexagon hidden">
          <h1 class="text-center pb-6">Hexgon</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div
              v-for="item in hexInfo"
              :key="item.Piece_Title"
              class="my-auto"
              witch="fit-content"
            >
              <!-- file information is loaded but need to add /assets/images/ to the src -->
              <a @click="ShowContentView(item.ID)"
                ><div
                  class="Peice rounded p-3 mx-auto my-4 sm:my-0 relative"
                  style="height: fit-content"
                >
                  <img
                    :src="`/Artwork/${item.Piece_Title}.jpg`"
                    alt="Art image"
                    class="rounded relative w-full"
                  />
                  <img
                    v-if="item.Sold"
                    src="/Artwork/SoldBanner.svg"
                    alt=""
                    class="w-inherit h-inherit absolute top-0 left-0"
                    style="height: -webkit-fill-available"
                  /></div
              ></a>
            </div>
          </div>
        </div>
        <div id="Portraits" class="Portraits hidden">
          <h1 class="text-center pb-6">Portraits</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div
              v-for="item in porInfo"
              :key="item.Piece_Title"
              class="my-auto"
              witch="fit-content"
            >
              <!-- file information is loaded but need to add /assets/images/ to the src -->
              <a @click="ShowContentView(item.ID)"
                ><div
                  class="Peice rounded p-3 mx-auto my-4 sm:my-0 relative"
                  style="height: fit-content"
                >
                  <img
                    :src="`/Artwork/${item.Piece_Title}.jpg`"
                    alt="Art image"
                    class="rounded relative w-full"
                  />
                  <img
                    v-if="item.Sold"
                    src="/Artwork/SoldBanner.svg"
                    alt=""
                    class="w-inherit h-inherit absolute top-0 left-0"
                    style="height: -webkit-fill-available"
                  /></div
              ></a>
            </div>
          </div>
        </div>
        <div id="AllArt" class="All">
          <h1 class="text-center pb-6">All My Pieces</h1>
          <div class="block sm:grid sm:grid-cols-3 gap-4">
            <div
              v-for="item in artworks"
              :key="item.Piece_Title"
              class="my-auto"
              witch="fit-content"
            >
              <!-- file information is loaded but need to add /assets/images/ to the src -->
              <a @click="ShowContentView(item.ID)"
                ><div
                  class="Peice rounded p-3 mx-auto my-4 sm:my-0 relative"
                  style="height: fit-content"
                >
                  <img
                    :src="`/Artwork/${item.Piece_Title}.jpg`"
                    alt="Art image"
                    class="rounded relative w-full"
                  />
                  <img
                    v-if="item.Sold"
                    src="/Artwork/SoldBanner.svg"
                    alt=""
                    class="w-inherit h-inherit absolute top-0 left-0"
                    style="height: -webkit-fill-available"
                  /></div
              ></a>
            </div>
          </div>
        </div>
        <ViewWork
          v-for="item in artworks"
          :key="item.Piece_Title"
          :digit="`${item.ID}`"
          :title="`${item.Piece_Title}`"
          :dimensions="`${item.Dimensions}`"
          :content="`${item.Blurb}`"
          :price="`${item.Price}`"
          :sold="`${item.Sold}`"
        />
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
    return {
      artworks,
      porInfo,
      hexInfo,
      lanInfo,
    }
  },
  methods: {
    ShowContentView(item) {
      const x = document.getElementById('VContainer' + item)
      if (x.style.display === 'none') {
        x.style.display = 'block'
      } else {
        x.style.display = 'none'
      }
      return item
    },
  },
}
</script>
