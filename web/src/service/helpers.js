import axios from 'axios'
import store from "../store/store";

const setFallBack = (http) => {
    http.interceptors.response.use((response) => {
        // Return a successful response back to the calling service
        return response;
    }, (error) => {
        // Return any error which is not due to authentication back to the calling service
        if (error.response.status !== 403) {
            store.commit('global/alert_user', error)
            store.commit('global/set_loading', false)
            return new Promise((resolve, reject) => {
                reject(error);
            });
        }


    });

    return http

}

const setLocalStorage = (payload) => {
    localStorage.setItem('token', payload.access)
    localStorage.setItem('refresh', payload.refresh)
    localStorage.setItem('username', payload.username)
    localStorage.setItem('image', payload.image)
}
const putToken = function () {
    let http = axios.create({})
    http.interceptors.request.use(config => {
        let token = localStorage.getItem('token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        } else {
            delete http.defaults.headers.common.Authorization;
        }
        return config
    })


    return setFallBack(http);

}


export default {
    putToken,
    setLocalStorage

}
