import helpers from "./helpers";
import store from "../store/store";
import Constants from "./Constants";

let http = helpers.putToken()


export default {
    GET_PROFILE(payload) {
         store.commit('search/setProfile',[])
        store.commit('global/set_loading', true)

        return http.get(`${Constants.API}${Constants.BACKEND_PROFILE}${payload.username}/`)
            .then(res => {
                store.commit('search/setProfile', res.data)
            }).catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            })
            .finally(() => {
                store.commit('global/set_loading', false)
            })
    },


}


