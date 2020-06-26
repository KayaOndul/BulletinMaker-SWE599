import Grids from "@/router/views/Grids";
import Login from "@/router/views/Login";
import Register from "@/router/views/Register";
import Home from "@/router/views/Home";
import Welcome from "@/router/views/Welcome";
import Search from "@/router/views/Search";
import Profile from "@/router/views/Profile";
export default [
    {
        path: '/',
        component: Home,
        children: [
            {
                name: 'Welcome',
                component: Welcome,
                path: ''
            },
            {
                name: 'report',
                path: 'report/:id',
                component: Grids,
            },
            {
                name: 'Search',
                path: 'search',
                component: Search
            },
            {
                name: 'Profile',
                path: 'profile',
                component: Profile

            }
        ]

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


    {path: '*', redirect: "/"}

]
