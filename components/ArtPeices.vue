<template>
  <div>
      <img :src="require(`../assets/images/${image}.jpg`)" alt="Art image">
    <div>
      <h1>{{ title }}</h1>
      <p>{{ content }}</p>
      <p>{{ dimensions }}</p>
      <p>${{ price }}</p>
    </div>
  </div>
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
      default: "5",
      required: true,
    },
  },
}
</script>
