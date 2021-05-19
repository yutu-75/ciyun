import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from "@/components/Home"
import WordCloud from "@/components/WordCloud";
Vue.use(Router)


export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Home',  //路由别名  url('',name='')
      component: Home,
    },
    {
      path: '/ciyun',
      name: 'WordCloud',  //路由别名  url('',name='')
      component: WordCloud,
    }
  ]
})
