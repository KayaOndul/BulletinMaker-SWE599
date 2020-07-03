import Grids from "@/router/views/Grids";
import Login from "@/router/views/Login";
import Register from "@/router/views/Register";
import Welcome from "@/router/views/Welcome";
import Search from "@/router/views/Search";
import Profile from "@/router/views/Profile";
import MyFollow from "./views/MyFollow";
import MyFresh from "./views/MyFresh"
import MyReports from "./views/MyReports"
import ChangePass from "./views/ChangePass"
import UserFollow from "./views/UserFollow"
import UserReports from "./views/UserReports"
import FollowList from "./views/FollowList"

export default [

    {
        component: Welcome,
        path: '/',
        redirect: 'MyFresh',
        children: [
            {
                name: 'MyReport',
                path: 'myreport',
                component: MyReports

            },
            {
                name: 'MyFollow',
                path: 'subscriptions',
                component: MyFollow,

            },
            {
                name: 'MyFresh',
                path: '',
                component: MyFresh,

            }
        ]
    },
    {
        name: 'report',
        path: '/report/:id',
        component: Grids,
    },
    {
        name: 'Search',
        path: '/search/:searchparam',
        component: Search
    },
    {
        name: 'Profile',
        path: '/profile/:username/',
        component: Profile,
        redirect: {
            name: 'UserReports'
        },
        children: [

            {

                name: 'UserReports',
                path: 'reports',
                component: UserReports

            },
            {
                name: 'UserFollow',
                path: 'subscriptions',
                component: UserFollow,

            },
            {
                name: 'Friends',
                path: 'friends',
                component: FollowList,

            },


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
    {
        name: 'ChangePassword',
        path: '/passwordChange',
        component: ChangePass
    },


    {path: '*', redirect: '/'}

]
