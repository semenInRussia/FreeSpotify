<template>
  <div id="app" class="main">
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">

    <v-app>
      <header-view></header-view>
      <v-main>
        <v-row
            align="center"
        >
          <v-container>
            <v-card elevation="12" class="main-card">
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
  padding: 10px;
}
</style>
