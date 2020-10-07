<template>
  <div>
    <header-view></header-view>

    <main>
      <router-view>

      </router-view>
    </main>
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
