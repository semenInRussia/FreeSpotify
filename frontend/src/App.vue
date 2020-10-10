<template>
  <div id="app">
    <v-app>
      <header-view></header-view>
      <v-main app>
        <v-row
            align="center"
        >
          <v-container>
            <router-view></router-view>
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
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

* {
  font-family: Arial, Harrington, serif;
}
</style>
