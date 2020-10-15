import Vue from "vue";
import VueRouter from "vue-router";

const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "index",
            meta: {},
            component: () => import("./components/pages/index.vue")
        },
        {
            path: "/top",
            name: "top",
            meta: {},
            component: () => import("./components/pages/WatchTop.vue"),
        },
        {
            path: "/artists/:artist_name",
            name: "artist_detail",
            meta: {},
            component: () => import("")
        },
        {
            path: "*",
            name: "page404",
            meta: {},
            component: () => import("./components/pages/page404")
        },
    ],
});

export default router;

Vue.use(VueRouter);
