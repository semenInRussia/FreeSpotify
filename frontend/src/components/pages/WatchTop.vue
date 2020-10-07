<template>
  <h1>Hello world!!!!!!!!!!!!!!!!!</h1>
</template>

<script>
import Layout from "@/Layout";

const base_url = ``
const url = `${base_url}/api/tracks/top`

export default {
  name: "WatchTop",

  data() {
    return {
      tracks: null,
      artist_url: null,
      artist_name: "ac dc",
    }
  },
  components: {
    Layout
  },
  mounted() {
    // set url
    this.artist_url = url + this.artist_name

    axios
        .get(this.artist_url)
        .then(response => (this.tracks = response));
  },
}
</script>

<style scoped>

</style>