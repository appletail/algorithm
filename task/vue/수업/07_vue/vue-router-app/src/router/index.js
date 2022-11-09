import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import DogView from '@/views/DogView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'


Vue.use(VueRouter)

const isLoggedIn = false

const routes = [
  {
    // url
    path: '/',
    name: 'home',
    // 처음 접속할 때 미리 로딩해놓는 방식
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // 처음 접속할 때 로딩을 안하는 방식
    // 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    // 동적 url
    // :userName 부분이 동적으로 변함
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인함')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = false
//   const authPages = ['hello']
//   const isAuthRequired = authPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log('Login으로 이동!')
//     next({ name: 'login' })
//   } else {
//     console.log('to로 이동!')
//     next()
//   }
// })


export default router
