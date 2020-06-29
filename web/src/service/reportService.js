import Constants from "./Constants";
import helpers from "./helpers";
import store from "../store/store";
import router from "../router/router";

let http = helpers.putToken()


export default {
    CREATE_REPORT() {
        store.commit('global/set_loading', true)
        const idStored = store.state.report.report.id
        store.commit('report/resetState',)
        return http({
            url: `${Constants.API}${Constants.BACKEND_REPORT_POST}`,
            method: "POST",
        }).then(
            res => {
                const id = idStored
                if (id && !store.state.report.report.layout) {
                    this.DELETE_REPORT({id})
                }
                store.commit('report/setReportNumber', res.data)
                store.commit('report/setReport', res.data)
                store.commit('global/set_alert', `Report created`)
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
    GET_ALL_REPORTS() {
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
    GET_ALL_REPORTS_VIA_USERNAME(payload) {

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
    GET_SUBSCRIBED_REPORTS(payload) {
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
                router.push({name: 'MyReport'})
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
                store.commit('global/set_alert', ` Report ${payload.id} ${res.data.detail}`)

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

