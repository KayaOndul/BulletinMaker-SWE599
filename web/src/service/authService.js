import CONSTANTS from "./Constants";
import store from "../store/store";
import helpers from "./helpers";

let http = helpers.putToken()




export default {
    REGISTER(payload) {
        store.commit('global/set_loading',true)
        return http.post(CONSTANTS.API + CONSTANTS.BACKEND_REGISTER, payload)
            .then(resp => {
                store.commit('auth/auth_success', resp.data)
                helpers.setLocalStorage(resp.data)
            }).catch(err => {
                store.dispatch('global/alertUser', err).then(err => err)
            })
            .finally(()=>{
                store.commit('global/set_loading',false)
            })

    },
    LOGIN(payload) {
        store.commit('global/set_loading',true)
        return http.post(CONSTANTS.API + CONSTANTS.BACKEND_LOGIN, payload)
            .then(resp => {
                store.commit('auth/auth_success', resp.data)
                helpers.setLocalStorage(resp.data)
            }).catch(err => {
                store.dispatch('global/alertUser', err).then(err => err)
            })  .finally(()=>{
                store.commit('global/set_loading',false)
            })


    },
    LOGOUT() {
        store.commit('global/set_loading',true)
        store.commit('auth/log_out')
        localStorage.clear()
        delete http.defaults.headers.common['Authorization']
        store.commit('global/set_loading',false)

    },



}


