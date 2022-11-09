import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    // 404에서 걸려서 detail로 가버리기 때문에 detail보다 위에 둠 혹은 문자열로 시작하도록 바꿔도 됨
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    // 아래의 redirect가 없더라도 잘못입력해도 종착지는 여기이기 때문에 404로 가짐
    // 만약 마지막이 아니라면 아래의 redirect를 적어놓아야함
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '*',
    redirect: { name: 'NotFound404'}
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
