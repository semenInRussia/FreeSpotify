<template>
  <div>
      {{ tracks }}
    <hr>
  </div>
</template>

<script>
import Layout from "@/Layout";
import axios from "axios";

const base_url = `http://localhost:8000`
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
    this.artist_url = url + "/" + this.artist_name

    axios
        .get(this.artist_url)
        .then(response => (this.tracks = response));
  },
}
</script>

<style scoped>

</style>