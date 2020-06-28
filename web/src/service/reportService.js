import Constants from "./Constants";
import helpers from "./helpers";
import store from "../store/store";
import router from "../router/router";

let http = helpers.putToken()


export default {
    CREATE_REPORT() {
        store.commit('global/set_loading', true)

        return http({
            url: `${Constants.API}${Constants.BACKEND_REPORT_POST}`,
            method: "POST",
        }).then(
            res => {
                store.commit('report/setReportNumber', res.data)
                  store.commit('global/set_alert', `${res.status} ${res.statusText}`)
            }
        )

            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },
    PATCH_REPORT(payload) {
        store.commit('global/set_loading', true)

        return http({
            url: `${Constants.API}${Constants.BACKEND_REPORT_POST}${payload.id}`,
            method: "PATCH",
            data: payload
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                store.commit('report/setReport', res.data)
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },
    GET_ALL_REPORTS(){
            store.commit('global/set_loading', true)
        return http({
            url: `${Constants.API}${Constants.BACKEND_ALL_REPORTS}`,
            method: "GET",
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                store.commit('report/setReports', res.data)
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },
    GET_ALL_REPORTS_VIA_USERNAME(payload){

            store.commit('global/set_loading', true)
        return http({
            url: `${Constants.API}${Constants.BACKEND_ALL_REPORTS_VIA_USERNAME}${payload.user}/`,
            method: "GET",
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                store.commit('report/setReports', res.data)
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },
    GET_SUBSCRIBED_REPORTS(payload){
              store.commit('global/set_loading', true)
        return http({
            url: `${Constants.API}${Constants.BACKEND_SUBSCRIBED_REPORTS}${payload.user}`,
            method: "GET",
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                store.commit('report/setReports', res.data)
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },


    GET_REPORT(payload) {
        store.commit('global/set_loading', true)
        return http({
            url: `${Constants.API}${Constants.BACKEND_REPORT_POST}${payload.id}`,
            method: "GET",
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                store.commit('report/setReport', res.data)
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    },
    DELETE_REPORT(payload) {
        store.commit('global/set_loading', true)
        return http({
            url: `${Constants.API}${Constants.BACKEND_REPORT_POST}${payload.id}`,
            method: "DELETE",
        }).then(
            res => {
                store.commit('global/set_alert', `${res.status}  ${res.statusText}`)
                router.push({name: 'Welcome'})
            }
        )
            .catch(err => {
                const error = err.response.data.error
                store.commit('global/set_alert', `${err.response.status} ${error}`)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    }
}

