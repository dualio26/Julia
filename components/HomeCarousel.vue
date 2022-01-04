<template>
  <div class="carousel max-h-24" aria-label="Gallery">
    <ol class="carousel__viewport">
      <li
        id="carousel__slide1"
        tabindex="0"
        class="carousel__slide"
        style="background-color: rgba(0, 0, 0, 0)"
      >
        <div class="carousel__snapper">
          <img
            :src="require(`../assets/images/${image1}.jpg`)"
            alt=""
            class="mx-auto"
            style="height: inherit"
          />
          <a href="#carousel__slide4" class="carousel__prev"></a>
          <a href="#carousel__slide2" class="carousel__next"></a>
        </div>
      </li>
      <li
        id="carousel__slide2"
        tabindex="0"
        class="carousel__slide"
        style="background-color: rgba(0, 0, 0, 0)"
      >
        <div class="carousel__snapper"></div>
        <img
            :src="require(`../assets/images/${image2}.jpg`)"
            alt=""
            class="mx-auto"
            style="height: inherit"
          />
        <a href="#carousel__slide1" class="carousel__prev"></a>
        <a href="#carousel__slide3" class="carousel__next"></a>
      </li>
      <li
        id="carousel__slide3"
        tabindex="0"
        class="carousel__slide"
        style="background-color: rgba(0, 0, 0, 0)"
      >
        <div class="carousel__snapper"></div>
        <img
            :src="require(`../assets/images/${image3}.jpg`)"
            alt=""
            class="mx-auto"
            style="height: inherit"
          />
        <a href="#carousel__slide2" class="carousel__prev"></a>
        <a href="#carousel__slide4" class="carousel__next"></a>
      </li>
      <li
        id="carousel__slide4"
        tabindex="0"
        class="carousel__slide"
        style="background-color: rgba(0, 0, 0, 0)"
      >
        <div class="carousel__snapper"></div>
        <img
            :src="require(`../assets/images/${image4}.jpg`)"
            alt=""
            class="mx-auto"
            style="height: inherit"
          />
        <a href="#carousel__slide3" class="carousel__prev"></a>
        <a href="#carousel__slide1" class="carousel__next"></a>
      </li>
    </ol>
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
    image4: {
      type: String,
      default: 'placeholder',
      required: false,
    },
  },
}
</script>