import router from "./router";
import Vue from "vue";
import Layout from "@/Layout";

new Vue({
    router,
    render: (h) => h(Layout),
}).$mount("#app");

console.log("OK...")