import axios from 'axios'





// const setFallBack = function (http) {
//     http.interceptors.response.use((response) => {
//         // Return a successful response back to the calling service
//         return response;
//     }, (error) => {
//         // Return any error which is not due to authentication back to the calling service
//         if (error.response.status !== 403) {
//             return new Promise((resolve, reject) => {
//                 localStorage.clear()
//                 reject(error);
//             });
//         }
//
//         // Logout user if token refresh didn't work or user is disabled
//         if (error.config.url == CONSTANTS.API+CONSTANTS.BACKEND_REFRESH||error.response.status===403) {
//
//             localStorage.clear();
//             router.push({name:'Login'}).then(r => r);
//
//             return new Promise((resolve, reject) => {
//                 reject(error);
//             });
//         }
//
//         // Try request again with new token
//
//
//         const refresh = localStorage.getItem('refresh')
//
//
//         return http.post(CONSTANTS.API + CONSTANTS.BACKEND_REFRESH, {refresh})
//             .then(resp => {
//                 store.commit('change_token', resp.data)
//             }).catch(err => {
//
//                 const status = err.response.status
//                 const detail = err.response.data.detail
//                 store.dispatch('global/alertUser', {status, detail}).then(err => err)
//             })
//             .then(() => {
//
//                 // New request with new token
//                 const config = error.config;
//                 config.headers['Authorization'] = `Bearer ${localStorage.getItem('token')}`;
//
//                 return new Promise((resolve, reject) => {
//                     http.request(config).then(response => {
//                         setLocalStorage(response.data)
//                         resolve(response);
//                     }).catch((error) => {
//                         reject(error);
//                     })
//                 });
//
//             })
//             .catch((error) => {
//                 Promise.reject(error);
//             });
//     });
//
//     return http
//
// }

const setLocalStorage = (payload) => {
    localStorage.setItem('token', payload.access)
    localStorage.setItem('refresh', payload.refresh)
    localStorage.setItem('username', payload.username)
    localStorage.setItem('image', payload.image)
}
const putToken = function () {
    let http=axios.create({})
    http.interceptors.request.use(config=>{
        let token = localStorage.getItem('token')
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        } else {
            delete http.defaults.headers.common.Authorization;
        }
        return config
    })




    return http;

}



export default {
    putToken,
    setLocalStorage

}