import helpers from "./helpers";
import store from "../store/store";
import Constants from "./Constants";

let http = helpers.putToken()


export default {
    LIKE(payload) {

        store.commit('global/set_loading', true)

        return http.post(Constants.API + Constants.BACKEND_LIKE, payload)
            .then(res => {
                store.commit('global/set_alert', `${res.status} ${res.data.detail}`)
            }).catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            })
            .finally(() => {
                store.commit('global/set_loading', false)
            })
    },


}


