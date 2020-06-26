import helpers from "@/service/helpers";

const getDefaultState = () => {
    return {
        refresh: localStorage.getItem('refresh') || '',
        token: localStorage.getItem('token') || '',
        username: localStorage.getItem('username') || '',


    }
}

export default {
    namespaced: true,
    state: getDefaultState(),
    mutations: {

        auth_success(state, payLoad) {
            helpers.setLocalStorage(payLoad)
            state.token = payLoad.access;
            state.refresh = payLoad.refresh
            state.username = payLoad.username
        },

        log_out(state) {
            localStorage.clear()
            Object.assign(state, getDefaultState())
        },
        change_token(state, payload) {
            state.token = payload.access
            localStorage.removeItem('token')
            localStorage.setItem('token', payload.access)

        },
        resetState(state) {
            // Merge rather than replace so we don't lose observers
            // https://github.com/vuejs/vuex/issues/1118
            Object.assign(state, getDefaultState())
        }


    },
    actions: {},
    getters: {
        isLoggedIn: (state) => !!state.token,
        username: (state) => state.username,


    }
}
