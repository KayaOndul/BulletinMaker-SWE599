const getDefaultState = () => {
    return {
        reportNumber: [],
        report: [],
        reports: [],

    }
}

// initial state
const state = getDefaultState()


const mutations = {
    setReports(state, payload) {
        state.reports = payload
    },
    setReport(state, payload) {
        state.report = payload
    },
    setReportNumber(state, payload) {
        state.reportNumber = payload.id
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
    actions: {},
    mutations
}
