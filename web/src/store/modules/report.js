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
        state.report = {...payload, title: payload.title==='[]' ? '' : payload.title}
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


const getters = {
    getReports(state){
        return state.reports?state.reports:[]
    }
}


export default {


    namespaced: true,
    state,
    getters,
    actions: {},
    mutations
}
