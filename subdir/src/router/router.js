import Vue from 'vue'
import Router from 'vue-router'
import routes from "./routes";
Vue.use(Router)

const router = new Router({
        name: 'router',
        mode: 'history',
        routes:routes
    }
)

export default router;