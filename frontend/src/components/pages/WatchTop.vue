<template>
  <div>
    {{ tracks }}
    <hr>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";


export default {
  name: "WatchTop",

  mounted() {
    this.fetchTop("ac dc")
  },
  methods: mapActions([`fetchTop`]),
  computed: mapGetters([`tracks`])

}
</script>

<style scoped>

</style>