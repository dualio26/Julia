<template>
  <div
    :id="`VContainer${digit}`"
    class="hidden VContainer fixed top-0 w-full h-full left-0"
  >
    <div class="View mx-auto rounded">
      <div class="grid grid-cols-2">
        <h1 class="text-4xl" style="width: fit-content">{{ title }}</h1>
        <a
          class="Close"
          style="height: fit-content; width: fit-content"
          @click="hideView(digit)"
          ><i class="fas fa-times fa-2x"></i
        ></a>
      </div>
      <div class="block sm:grid grid-cols-2 pt-12">
        <div class="h-full">
          <h2>Description:</h2>
          <p class="mb-12">{{ content }}</p>
          <h2>Dimensions:</h2>
          <p>{{ dimensions }}</p>
          <h2>Price:</h2>
          <p>{{ price }}</p>
        </div>
        <div class="h-full my-auto mx-auto relative w-full" >
          <img :src="`/Artwork/${title}.jpg`" alt="Peice Image" class="rounded relative"/>
          <img
            v-if="`${sold}`"
            src="/Artwork/SoldBanner.svg"
            alt=""
            class="w-inherit h-inherit absolute top-0 left-0"
            style="height: -webkit-fill-available"
          />
        </div>
      </div>
      <PurButton title="Purchase" :piece="`${title}`" />
    </div>
  </div>
</template>

<script>
import data from '~/content/blog.json'
export default {
  props: {
    title: {
      type: String,
      default: '',
      required: true,
    },
    dimensions: {
      type: String,
      default: '',
      required: true,
    },
    content: {
      type: String,
      default: '',
      required: true,
    },
    price: {
      type: String,
      default: '',
      required: true,
    },
    digit: {
      type: String,
      default: '',
      required: true,
    },
    sold: {
      type: String,
      default: '',
      required: true,
    },
  },

  data() {
    return {
      data,
    }
  },
  methods: {
    hideView(ID) {
      const x = document.getElementById('VContainer' + ID)
      if (x.style.display === 'none') {
        x.style.display = 'block'
      } else {
        x.style.display = 'none'
      }
    },
  },
}
</script>

<style>
.VContainer {
  background-color: rgba(0, 0, 0, 0.5);
}

.View {
  padding: 2%;
  margin-top: 2%;
  width: 95%;
  height: 95%;
  background-color: #ddd;
}

.Close {
  margin-left: 96%;
}

@media only screen and (max-width: 320px) {
  .Close {
    margin-left: 80%;
  }
}
</style>
