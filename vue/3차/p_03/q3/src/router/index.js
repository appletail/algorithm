import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NocolorView from '../views/NocolorView.vue'
import HapplingView from '../views/HapplingView.vue'
import HapplossomeView from '../views/HapplossomeView.vue'
import HapplowerView from '../views/HapplowerView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/happeed',
    name: 'happeed',
    component: NocolorView
  },
  {
    path: '/happling',
    name: 'happling',
    component: HapplingView
  },
  {
    path: '/happlossome',
    name: 'happlossome',
    component: HapplossomeView
  },
  {
    path: '/happlower',
    name: 'happlower',
    component: HapplowerView
  },
  {
    path: '/notfound',
    name: 'notfound',
    component: NotFound404
  },
  {
    path: '*',
    redirect: { name: 'notfound' }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

router.beforeEach((to, from, next) => {
  if (to.name === 'happlossome' && from.name === 'happlower') {
    alert('이전 진화 단계로 돌아갈 수 없습니다.')
    return
  } else if (to.name === 'happling' && from.name === 'happlossome') {
    alert('이전 진화 단계로 돌아갈 수 없습니다.')
    return
  } else if (to.name === 'happeed' && from.name === 'happling') {
    alert('이전 진화 단계로 돌아갈 수 없습니다.')
    return
  } else if (to.name === 'home' && from.name === 'happlower') {
    alert('Home으로 돌아갑니다!')
  }
  next()
})