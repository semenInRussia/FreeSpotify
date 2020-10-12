import router from "./router";
import Vue from "vue";
import Layout from "@/App";
import store from "@/store";
import vuetify from "@/plugins/vuetify";

new Vue({
    router,
    store,
    vuetify,
    render: (h) => h(Layout),
}).$mount("#app");