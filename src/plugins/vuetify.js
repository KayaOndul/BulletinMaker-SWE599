import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  breakpoint: {
    thresholds: {
      xs: 420,
      sm: 540,
      md: 800,
      lg: 1280,
    },
    scrollBarWidth: 24,
  },
  icons: {
    iconfont: 'mdiSvg',
  },

  theme: {
    themes: {
      light: {
        primary: '#45bd8b',
        secondary: '#424242',
        accent: '#803eff',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107'
      },
    },
  },
});
