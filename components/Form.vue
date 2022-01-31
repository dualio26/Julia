<template>
  <div class="w-3/4 mx-auto">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <form href="mailto:eamongreen59@gmail.com">
      <div class="form-group">
        <label for="exampleFormControlInput1">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleFormControlInput1"
          placeholder="name@example.com"
        />
      </div>
      <div class="form-group">
        <label for="exampleFormControlSelect1">Example select</label>
        <select class="form-control" placeholder="Art Peice" required>
          <option value="" disabled selected hidden class="opacity-25">
            Choose a Art Work
          </option>
          <option v-for="item in TheInfo" :key="item.Piece_Title">
            {{ item.Piece_Title }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">Example textarea</label>
        <textarea
          class="form-control"
          id="exampleFormControlTextarea1"
          rows="3"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary mt-12">Submit</button>
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