<template>
  <div class="slides pt-8">
    <div>
      <img :src="`/Artwork/${image1}.jpg`" alt="" class="rounded" />
    </div>

    <div>
      <img :src="`/Artwork/${image2}.jpg`" alt="" class="rounded" />
    </div>

    <div>
      <img :src="`/Artwork/${image3}.jpg`" alt="" class="rounded" />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    image1: {
      type: String,
      default: 'placeholder',
      required: false,
    },
    image2: {
      type: String,
      default: 'placeholder',
      required: false,
    },
    image3: {
      type: String,
      default: 'placeholder',
      required: false,
    },
  },
}
</script>

<style>
.slides {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.slides > div {
  display: flex;
  flex-shrink: 0;
  width: 100%;
  height: 500px;
  scroll-snap-align: start;
  scroll-behavior: smooth;
  justify-content: center;
  align-items: center;
  font-size: 100px;
}

.slides div img {
  height: inherit;
}

@media screen and (max-width: 768px) {
  .slides div img {
    height: auto;
  }
}
</style>
