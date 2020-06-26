import CONSTANTS from "./Constants";
import helpers from "./helpers";
import store from "../store/store";

let http = helpers.putToken()


export default {
    SEARCH(payload) {
        if(!payload){
            return
        }
        store.commit('global/set_loading', true)
        return http.get(`${CONSTANTS.API}${CONSTANTS.BACKEND_SEARCH}${payload}`)
            .then(res => {
                store.commit('global/setSearchResponse', res.data)
            }).catch(err => {
                store.dispatch('global/alertUser', err)
            })
            .finally(() => {
                store.commit('global/set_loading', false)
            })
    },


}


