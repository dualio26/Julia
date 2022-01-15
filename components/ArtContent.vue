<template>
  <div id="AllContnet">
    <div class="pt-12 mx-auto w-10/12 block">
      <div id="Landscape" class="Landscape hidden">
        <h1 class="text-center">Landscape</h1>
        <div id="AboutContent" class="hidden sm:grid grid-cols-3">
          <ArtPeices
            image="image0"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          /><ArtPeices
            image="image1"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          /><ArtPeices
            image="image2"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          />
          <ArtPeices
            image="image0"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          /><ArtPeices
            image="image1"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          /><ArtPeices
            image="image2"
            title="First Peice"
            content="About the peice"
            dimensions="(x+2)(x-2)"
            price="123"
          />
        </div>
      </div>
      <div id="Hexagon" class="Hexagon hidden">
        <h1 class="text-center">Hexgon</h1>
        <p id="HexagonContent"></p>
      </div>
      <div id="Portraits" class="Portraits hidden">
        <h1 class="text-center">Portraits</h1>
        <p id="PortraitContent"></p>
      </div>
      <div id="AllArt" class="All hidden">
        <h1 class="text-center">All My Pieces</h1>
        <p id="AllContent">all Content</p>
      </div>
    </div>
  </div>
</template>
