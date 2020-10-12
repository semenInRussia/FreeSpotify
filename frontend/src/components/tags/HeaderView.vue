<template>
  <div id="nav">
    <div class="ma-12 pa-12">

      <v-card>
        <v-navigation-drawer
            permanent
            expand-on-hover
            app
        >

          <v-list>
            <v-list-item link href="/">
              <v-list-item-content>
                <v-list-item-title>FreeSpotify</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-list
              nav
              dense
          >
            <v-list-item link href="/top">
              <v-list-item-icon>
                <v-icon>mdi-folder</v-icon>
              </v-list-item-icon>
              <v-list-item-content>Top</v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-card>
    </div>
  </div>
</template>

<script>

import Vuetify from "vuetify";

export default {
  name: "HeaderView",
  vuetify: new Vuetify(),
  methods: {
    UpdateTop(artist_name) {
      this.$emit('update-top', artist_name)
    }
  }
}
</script>

<style scoped>
.text-input {
  border-radius: 6px;
  display: inline-block;
  padding: 5px;
}

.navbar {
  background-color: midnightblue;
  margin: 0;

  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
}

.navbar-brand {
  margin: 10px;
  color: white;
  font-size: 20px;
  text-decoration: none;
}

.navbar-brand:hover {
  color: darkturquoise;
}

.navbar-nav {
  list-style-type: none;
  grid-gap: 10px;
}

.nav-link {
  text-decoration: none;
  color: white;
}

.nav-link:hover {
  color: darkgoldenrod;
}
</style>