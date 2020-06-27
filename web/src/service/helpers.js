import axios from 'axios'


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


    return http

}


export default {
    putToken,
    setLocalStorage

}
