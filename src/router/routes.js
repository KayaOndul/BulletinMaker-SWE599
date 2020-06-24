import Grids from "@/router/views/Grids";
import Login from "@/router/views/Login";
import Register from "@/router/views/Register";

export default [
    {
        name: 'Home',
        path: '/',
        component: Grids,
    },
    {
        name: 'Login',
        path: '/Login',
        component: Login
    },
    {
        name: 'Register',
        path: '/Register',
        component: Register
    },


    {path: '*', redirect:'/'}

]
