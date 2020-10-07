<template>
  <nav class="navbar">
    <a class="navbar-brand" href="/">FreeSpotify</a>

    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="">TOP</a>
      </li>
    </ul>


    <form class="nav__form">
      <label>
        <input placeholder="Search:" class="text-input">
      </label>
      <ButtonSubmit class="success-outline" value="Search"></ButtonSubmit>
    </form>
  </nav>
</template>

<script>
import ButtonSubmit from "./b-submit";
import TextInput from "@/components/tags/TextInput";

export default {
  name: "HeaderView",
  components: {
    ButtonSubmit,
    TextInput
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