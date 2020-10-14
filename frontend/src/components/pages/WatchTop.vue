<template>
  <div>
    <v-alert
        color="red"
        outlined
        prominent
        text
        type="error"

        v-if="tracks.error_name"
    >
      {{ tracks.error_description }}
    </v-alert>
    <form @submit.prevent="updateTop()">
      <v-text-field v-model="artist_name"></v-text-field>
      <v-btn color="primary" type="submit">Search</v-btn>
    </form>

    <br>
    <v-progress-linear v-if="loading" :value="value"></v-progress-linear>
    <br>

    <v-list v-if="!tracks.error_name">
      <v-list-item v-for="track in tracks" :key="track.top_number">
        <v-list-item-title>{{ track.top_number }} | {{ track.name }}</v-list-item-title>
        <v-list-item-subtitle>
          <a :href="track.artist_link">{{ track.artist_name }}</a>
        </v-list-item-subtitle>

        <v-list-item-subtitle>
          <a :href="track.album_link">{{ track.album_name }}</a> {{ track.release_date }}
        </v-list-item-subtitle>

        <v-list-item-avatar tile>
          <img :src="track.album_img_link" alt="ALBUM">
        </v-list-item-avatar>
        <v-divider></v-divider>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";


export default {
  name: "WatchTop",
  data: () => {
    return {
      artist_name: null,
      value: 15
    }
  },
  methods: {
    ...mapActions([`fetchTop`]),

    updateTop() {
      this.fetchTop(this.artist_name)
    },
  },
  computed: mapGetters([`tracks`, `loading`])

}
</script>

<style scoped>

</style>