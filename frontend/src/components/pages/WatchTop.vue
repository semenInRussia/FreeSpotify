<template>
  <div>
    <form @submit.prevent="updateTop()">
      <v-text-field v-model="artist_name"></v-text-field>
      <v-btn color="primary" type="submit">Search</v-btn>
    </form>

    <br>
    <v-progress-linear v-if="is_show_loader" :value="value"></v-progress-linear>
    <br>

    <v-list>
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
      is_show_loader: true,
      value: 15
    }
  },
  methods: {
    ...mapActions([`fetchTop`]),

    updateTop() {
      this.showLoader()
      this.fetchTop(this.artist_name)
      this.hideLoader()
    },
    showLoader() {
      this.is_show_loader = true
    },
    hideLoader() {
      this.is_show_loader = false
    }
  },
  computed: mapGetters([`tracks`])

}
</script>

<style scoped>

</style>