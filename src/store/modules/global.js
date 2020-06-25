const getDefaultState = () => {
    return {
        showAlertNotifications: true,
        alerts: [],
        loading: false,

    }
}

// initial state
const state = getDefaultState()

const actions = {
    resetState({commit}) {
        commit('resetState')
    },


    alertUser({commit}, payload) {
        commit('set_alert', payload)

    },
    removeAlert({commit}) {
        commit('remove_alert')
    },


}

const mutations = {


    set_loading(state, payload) {
        state.loading = payload
    },
    set_alert(state, payload) {
        const alert = state.alerts
        alert.push(payload)
        state.alerts = alert
    },
    remove_alert(state) {
        const alert = state.alerts
        alert.shift()

        state.alerts = alert
    },


    setAlert(state) {
        state.showAlertNotifications = false
    },

    resetState(state) {
        // Merge rather than replace so we don't lose observers
        // https://github.com/vuejs/vuex/issues/1118
        Object.assign(state, getDefaultState())
    }
}


const getters = {}


export default {


    namespaced: true,
    state,
    getters,
    actions,
    mutations
}