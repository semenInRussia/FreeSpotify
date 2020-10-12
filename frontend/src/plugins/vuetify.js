import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import dark from "@/vars"

Vue.use(Vuetify)

const opts = {
    theme: {
        dark: dark
    }
}

export default new Vuetify(opts)