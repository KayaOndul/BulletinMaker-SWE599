const getDefaultState = () => {
    return {
        searchResponse: [],
        profile: []

    }
}

// initial state
const state = getDefaultState()


const mutations = {
    setSearchResponse(state, payload) {
        state.searchResponse = payload
    },
    setProfile(state, payload) {
        state.profile = payload
    },

    resetState(state) {
        // Merge rather than replace so we don't lose observers
        // https://github.com/vuejs/vuex/issues/1118
        Object.assign(state, getDefaultState())
    }
}


const getters = {
    searchFeed(state) {
        if (state.searchResponse) {
            const list1 = state.searchResponse.users ? state.searchResponse.users.map(e => {
                return {
                    name: e.username,
                    id: e.id,
                    category: 'User',
                    component: 'Profile'

                }
            }) : []
            const list2 = state.searchResponse.reports ? state.searchResponse.reports.map(e => {
                return {
                    name: e.title,
                    id: e.id,
                    owner: e.owner,
                    category: 'Report',
                    component: 'Report'

                }
            }) : []

            const payload = list1.concat(list2)
            return payload
        }
        return []

    }
}


export default {


    namespaced: true,
    state,
    getters,
    actions: {},
    mutations
}
