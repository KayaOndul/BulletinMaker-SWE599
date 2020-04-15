import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router/router'
import store from './store/store'



// Styles

import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import "@/assets/global.scss"





Vue.config.productionTip = false

new Vue({

  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')

