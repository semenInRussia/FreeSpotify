import Vue from "vue";
import Vuex from "vuex";
import Top from "./modules/Top";

Vue.use(Vuex)


export default new Vuex.Store({
    modules: {
        Top
    }
});

