<template>
  <div>
    <form>
      <v-text-field v-model="artist_name"></v-text-field>
      <v-btn color="primary" @click="fetchTop(artist_name)">Search</v-btn>
    </form>

    <br>

    <v-list v-for="track in tracks">
      <v-list-item-title>{{ track.top_number }} | {{track.name }}</v-list-item-title>
      <v-list-item-subtitle>
        <a :href="track.artist_link">{{ track.artist_name}}</a>
      </v-list-item-subtitle>

      <v-list-item-content>
        <a :href="track.album_link">{{ track.album_name }}</a> {{ track.release_date }}
      </v-list-item-content>
      <v-divider></v-divider>
    </v-list>
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
  methods: mapActions([`fetchTop`]),
  computed: mapGetters([`tracks`])

}
</script>

<style scoped>

</style>