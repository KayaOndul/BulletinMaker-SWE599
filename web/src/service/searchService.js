import helpers from "./helpers";
import store from "../store/store";
import Constants from "./Constants";

let http = helpers.putToken()


export default {
    SEARCH(payload) {

        store.commit('global/set_loading', true)
        return http.post(Constants.API + Constants.SEARCH_ENDPOINT, payload)
            .then(res => {
                store.commit('search/setSearchResponse', res.data)
            }).catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            })
            .finally(() => {
                store.commit('global/set_loading', false)
            })
    },


}


