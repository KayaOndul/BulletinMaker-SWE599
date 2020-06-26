import Constants from "./Constants";
import helpers from "./helpers";
import store from "../store/store";

let http = helpers.putToken()


export default {
    SAVE_REPORT(payload) {
        store.commit('global/set_loading', true)

        return http.post({
            url: `${Constants.API}${Constants.BACKEND_REPORT}`,
            data: payload,
        })
            .then(res => {
                store.commit('global/alertUser', res.status)
            }).catch(err => {
                store.dispatch('global/alertUser', err)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    }
}

