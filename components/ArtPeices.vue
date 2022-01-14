<template>
  <a href="#" class="Peice rounded p-6">
    <img
      :src="require(`../assets/images/${image}.jpeg`)"
      alt="Art image"
      class="rounded-t"
    />
    <div class="pt-4">
      <h1>{{ title }}</h1>
      <p>{{ content }}</p>
      <p>{{ dimensions }} mm</p>
      <p>${{ price }}</p>
    </div>
  </a>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'The title',
      required: true,
    },
    content: {
      type: String,
      default: 'The content',
      required: true,
    },
    dimensions: {
      type: String,
      default: 'The dimensions',
      required: true,
    },
    image: {
      type: String,
      default: 'placeholder',
      required: false,
    },
    price: {
      type: String,
      default: '5',
      required: true,
    },
  },
}
</script>
