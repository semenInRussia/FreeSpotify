import Vue from "vue";
import VueRouter from "vue-router";

const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "top",
            meta: {},
            component: () => import("./components/pages/WatchTop.vue"),
        },
        {
            path: "*",
            name: "page404",
            meta: {},
            component: () => import("./components/pages/page404")
        }
    ],
});

export default router;

Vue.use(VueRouter);
