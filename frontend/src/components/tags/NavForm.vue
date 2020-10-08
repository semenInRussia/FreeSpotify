<template>
  <form class="nav__form" @submit.prevent="$emit('update-top', this.artist_name)">
    <label>
      <input placeholder="Search:" class="text-input" v-model="artist_name">
    </label>
    <ButtonSubmit class="success-outline" value="Search"></ButtonSubmit>
  </form>
</template>

<script>
import ButtonSubmit from "@/components/tags/ButtonSubmit";

export default {
  name: "NavForm",
  components: {
    ButtonSubmit
  },
  data: () => {
    return {
      artist_name: null,
    }
  },
}
</script>

<style scoped>

</style>