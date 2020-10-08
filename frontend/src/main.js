import router from "./router";
import Vue from "vue";
import Layout from "@/Layout";
import store from "@/store";


new Vue({
    router,
    store,
    render: (h) => h(Layout),
}).$mount("#app");