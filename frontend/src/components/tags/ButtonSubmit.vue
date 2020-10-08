<template>
  <input type="submit" class="button">
</template>

<script>
export default {
  name: "ButtonSubmit"
}
</script>

<style scoped>
.button {
  padding: 5px;
  border-radius: 8px;
  display: inline-block;
}

.success-outline {
  border-color: #00ff00;
  border-width: 3px;
  border-style: solid;

  text-decoration: none;
  font-size: large;

  color: lime;
  background-color: rgba(0, 0, 0, 0);

  margin-left: 3px;

  user-focus-pointer: painted;
}

.success-outline:hover {
  color: black;
  background-color: lime;

  transition: 1s;
}
</style>