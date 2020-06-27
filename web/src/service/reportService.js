import Constants from "./Constants";
import helpers from "./helpers";
import store from "../store/store";

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
            }
        )

            .catch(err => {
                store.commit('global/set_alert', err)
            }).finally(() => {
                store.commit('global/set_loading', false)
            })
    }
}

