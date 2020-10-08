<template>
  <nav class="navbar">
    <a class="navbar-brand" href="/">FreeSpotify</a>

    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="">TOP</a>
      </li>
    </ul>

    <NavForm @update-top=""></NavForm>

  </nav>
</template>

<script>
import ButtonSubmit from "./ButtonSubmit";
import TextInput from "@/components/tags/TextInput";
import NavForm from "@/components/tags/NavForm";

export default {
  name: "HeaderView",
  components: {
    ButtonSubmit,
    TextInput,
    NavForm
  },
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