import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import global from "@/store/modules/global";
import report from "./modules/report";
import search from "./modules/search";

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth,
        global,
        report,
        search
    },
})
