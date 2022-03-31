import Vue from 'vue';
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue'; // import lottie-vuejs
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.use(LottieAnimation); // add lottie-animation to your global scope

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
