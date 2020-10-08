import Vue from "vue";
import Vuex from "vuex";
import Top from "./modules/Top";

Vue.use(Vuex)


const store = new Vuex.Store({
    modules: {
        Top
    }
});

export default store
