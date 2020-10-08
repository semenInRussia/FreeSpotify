<template>
  <div>
    <input type="text" v-model="artist_name">
    <button @click="fetchTop(artist_name)">Search</button>

    <ul>
      <li v-for="track in tracks">
        <a :href="track.artist_link">{{ track.artist_name }}</a> <span>{{ track.name }}</span>
        <br>
        <a :href="track.album_link">{{ track.album_name }}</a> <span>{{ track.release_date }}</span>
        <hr>
      </li>
    </ul>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";


export default {
  name: "WatchTop",
  data: () => {
    return {
      artist_name: null
    }
  },
  mounted() {
    this.fetchTop(this.artist_name)
  },
  methods: mapActions([`fetchTop`]),
  computed: mapGetters([`tracks`])

}
</script>

<style scoped>

</style>