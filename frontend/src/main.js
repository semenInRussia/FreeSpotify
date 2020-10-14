import router from "./router";
import Vue from "vue";
import Layout from "@/App";
import store from "@/store";
import vuetify from "@/plugins/vuetify";
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

new Vue({
    router,
    store,
    vuetify,
    render: (h) => h(Layout),
}).$mount("#app");