<template>
  <div class="carousel max-h-24" aria-label="Gallery">
    <ol class="carousel__viewport">
      <li id="carousel__slide1" tabindex="0" class="carousel__slide">
        <div class="carousel__snapper">
          <a href="#carousel__slide4" class="carousel__prev"></a>
          <a href="#carousel__slide2" class="carousel__next"></a>
        </div>
      </li>
      <li id="carousel__slide2" tabindex="0" class="carousel__slide">
        <div class="carousel__snapper"></div>
        <a href="#carousel__slide1" class="carousel__prev"></a>
        <a href="#carousel__slide3" class="carousel__next"></a>
      </li>
      <li id="carousel__slide3" tabindex="0" class="carousel__slide">
        <div class="carousel__snapper"></div>
        <a href="#carousel__slide2" class="carousel__prev"></a>
        <a href="#carousel__slide4" class="carousel__next"></a>
      </li>
      <li id="carousel__slide4" tabindex="0" class="carousel__slide">
        <div class="carousel__snapper"></div>
        <a href="#carousel__slide3" class="carousel__prev"></a>
        <a href="#carousel__slide1" class="carousel__next"></a>
      </li>
    </ol>
  </div>
</template>
