import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '에스프레소',
        price: 3500,
        selected: true, // 초기값
        image: 'https://source.unsplash.com/featured/?espresso'
      },
      {
        title: '아메리카노',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
    ],
    sizeList: [
      {
        name: 'Short',
        price: -500,
        selected: false,
      },
      {
        name: 'Tall',
        price: 0,
        selected: true, // 초기값
      },
      {
        name: 'Grande',
        price: 500,
        selected: false,
      },
      {
        name: 'Venti',
        price: 100,
        selected: false,
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function (state, menu) {
      const idx = state.menuList.indexOf(menu)
      state.menuList[idx].selected = !state.menuList[idx].selected
    },
    updateSizeList: function () {},
  },
  actions: {
  },
  modules: {
  }
})