<template>
  <div id="app" class="main">
    <v-app>
      <header-view></header-view>
      <v-main>
        <v-row
            align="center"
        >
          <v-container>
            <v-card elevation="12" :loading="loading">
              <router-view></router-view>
            </v-card>
          </v-container>
        </v-row>
      </v-main>
    </v-app>
  </div>
</template>

<script>
import HeaderView from "./components/tags/HeaderView";

export default {
  name: "Layout",
  components: {
    HeaderView
  },
  data() {
    return {
      loading: false
    }
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

.main {
  background-image: url("https://townsquare.media/site/295/files/2015/03/80sTop1001.jpg");
  background-repeat: repeat;
}

.main-card {
  margin: 5px;
}
</style>
