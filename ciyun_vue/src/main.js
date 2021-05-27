// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'


// import header from '@/components/common/Header';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';

import settings from "./settings";
import router from './router/index'
Vue.use(ElementUI);

Vue.config.productionTip = false


// 调用插件
Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.prototype.$settings = settings;
axios.defaults.withCredentials = false;
// Vue.prototype.Header = header;


//复制
import VueClipboard from 'vue-clipboard2'
Vue.use( VueClipboard )

Vue.prototype.$axios = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
