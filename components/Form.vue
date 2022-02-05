<template>
  <div class="w-3/4 mx-auto">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <form action="mailto:juliasternkopfart@gmail.com" method="GET" enctype="text/plain">
      <div class="form-group">
        <label id="email" for="exampleFormControlInput1" name="email" >Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleFormControlInput1"
          placeholder="name@example.com"
        />
      </div>
      <div class="form-group">
        <label for="exampleFormControlSelect1">Select  an option</label>
        <select id="subject" class="form-control" placeholder="Art Peice" required name="subject" >
          <option value="" disabled selected hidden class="opacity-25">
            Choose an option
          </option>
          <option value="" class="opacity-25">
            Commisions
          </option>
          <option value="" class="opacity-25">
            Questions
          </option>
          <option v-for="item in TheInfo" :key="item.Piece_Title">
            {{ item.Piece_Title }}
          </option>
        </select>
      </div>
      <!-- <div class="form-group">
        <label for="exampleFormControlTextarea1">Example textarea</label>
        <textarea
          id="exampleFormControlTextarea1"
          class="form-control"
          name="body"
          rows="3"
        ></textarea>
      </div> -->
      <input type="submit" value="Send" class="btn btn-primary mt-12" style="background-color: #d0bebdfd; border-color: #d0bebdfd; color: black; font-family: Courier, monospace;" />
    </form>
  </div>
</template>

<script>
import data from '~/content/data.json'
export default {
  data() {
    const artworks = data
    const len = data.length
    let i = 0
    const TheInfo = []
    while (i !== len) {
      const temp = artworks[i]
      if (temp.Category === 'Hexagon') {
        TheInfo.push(temp)
      }
      if (temp.Category === 'Landscape') {
        TheInfo.push(temp)
      }
      if (temp.Category === 'Portrait') {
        TheInfo.push(temp)
      }
      i++
    }
    return {
      artworks,
      TheInfo,
    }
  },
}
</script>