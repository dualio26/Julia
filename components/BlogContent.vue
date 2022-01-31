<template>
  <div class="sm:grid grid-cols-1 w-3/4 mx-auto">
  <h1 class="text-center my-24 text-2xl">Blog</h1>
    <div v-for="item in blog" :key="item.Content" class="Peice rounded p-4 my-12 grid grid-cols-2 mx-auto">
      <div>
        <h1 id="demo-2" class="text-2xl pb-6">{{ item.Content }}...</h1>
        <p>{{ item.Content }}</p>
      </div>
      <div>
        <img
          :src="`/Artwork/${item.Image}.jpg`"
          alt="Blog image"
          class="rounded"
        />
      </div>
    </div>
  </div>
</template>

<script>
import data from '~/content/blog.json'
export default {
  data() {
    const blog = data
    return { blog }
  },
}
</script>

<style>
#demo-2 {
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>