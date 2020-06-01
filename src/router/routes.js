import Home from "@/router/views/Home";
import Grids from "@/router/Grids";

export default [
    {
        name: 'Home',
        path: '/Home',
        component: Home,
    },
    {
        name: 'Grids',
        path: '/Grids',
        component: Grids,
    },
    {path: '*', component: Grids}

]
