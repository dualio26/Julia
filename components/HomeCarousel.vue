<template>
  <div>
  <input type="radio" name="position" hidden />
  <input type="radio" name="position" checked hidden />
  <input type="radio" name="position" hidden />
  <main id="carousel">
    <div class="item"><img :src="`/Artwork/${image1}.jpg`" alt="" class="my-auto" style="justify-content:center;align-items:center;"></div>
    <div class="item"><img :src="`/Artwork/${image2}.jpg`" alt="" class="my-auto"></div>
    <div class="item"><img :src="`/Artwork/${image3}.jpg`" alt="" class="my-auto"></div>
    </main>
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

<style>

@keyframes display {
  0% {
    transform: translateX(200px);
    opacity: 0;
  }
  10% {
    transform: translateX(0);
    opacity: 1;
  }
  20% {
    transform: translateX(0);
    opacity: 1;
  }
  30% {
    transform: translateX(-200px);
    opacity: 0;
  }
  100% {
    transform: translateX(-200px);
    opacity: 0;
  }
}

main#carousel {
  grid-row: 1 / 2;
  grid-column: 1 / 8;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  transform-style: preserve-3d;
  perspective: 600px;

  --items: 5;
  --middle: 3;
  --position: 1;

  pointer-events: none;
}

div.item {
  position: absolute;
  width: 300px;
  height: 400px;

  --r: calc(var(--position) - var(--offset));
  --abs: max(calc(var(--r) * -1), var(--r));

  transition: all 0.25s linear;
  transform: rotateY(calc(-10deg * var(--r)))
    translateX(calc(-300px * var(--r)));
  z-index: calc((var(--position) - var(--abs)));
}

div.item:nth-of-type(1) {
  --offset: 1;

}
div.item:nth-of-type(2) {
  --offset: 2;
  
}
div.item:nth-of-type(3) {
  --offset: 3;

}

input:nth-of-type(1) {
  grid-column: 2 / 3;
  grid-row: 2 / 3;
}
input:nth-of-type(1):checked ~ main#carousel {
  --position: 1;
}

input:nth-of-type(2) {
  grid-column: 3 / 4;
  grid-row: 2 / 3;
}
input:nth-of-type(2):checked ~ main#carousel {
  --position: 2;
}

input:nth-of-type(3) {
  grid-column: 4 /5;
  grid-row: 2 / 3;
}
input:nth-of-type(3):checked ~ main#carousel {
  --position: 3;
}

</style>
