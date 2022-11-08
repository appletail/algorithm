import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '에스프레소',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?espresso'
      },
      {
        title: '아메리카노',
        price: 4100,
        selected: false, // 초기값
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '카페라떼',
        price: 4600,
        selected: false,
        image: 'https://source.unsplash.com/featured/?cafelatte'
      },
      {
        title: '콜드브루',
        price: 4500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?coldbrew'
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
        selected: false, // 초기값
      },
      {
        name: 'Grande',
        price: 500,
        selected: false,
      },
      {
        name: 'Venti',
        price: 1000,
        selected: false,
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0
      },
      {
        type: '바닐라 시럽',
        price: 500,
        count: 0
      },
      {
        type: '카라멜 시럽',
        price: 500,
        count: 0
      },
    ],
    tmpList: [0, 0, 0],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      return state.orderList.reduce((acc, cur) => {
        const options = cur.optionList.reduce((acc, cur) => {
          return acc + cur.price * cur.count
        }, 0)
        return acc += cur.menu.price + cur.size.price +options
      }, 0)
    }
  },
  mutations: {
    addOrder: function (state) {
      const order = {}
      state.menuList.forEach((elem) => {if (elem.selected) {order.menu = elem}})
      state.sizeList.forEach((elem) => {if (elem.selected) {order.size = elem}})
      const optionList = []
      state.optionList.forEach((elem) => {
        const tmpObj = {
          type: elem.type,
          price: elem.price,
          count: elem.count,
        }
        optionList.push(tmpObj)
      })
      order.optionList = optionList


      if (order.menu && order.size) {
        state.orderList.push(order)
  
        state.menuList.map((elem) => {elem.selected=false})
        state.sizeList.map((elem) => {elem.selected=false})
        state.optionList.map((elem) => {elem.count=0})
      }
    },
    updateMenuList: function (state, selectedMenu) {
      state.menuList.map((elem) => {
        if (elem === selectedMenu) {
          elem.selected = true
        } else {
          elem.selected = false
        }
      })
    },
    updateSizeList: function (state, selectedSize) {
      state.sizeList.map((elem) => {
        if (elem === selectedSize) {
          elem.selected = true
        } else {
          elem.selected = false
        }
      })
    },
    OPTION_INCREASE(state, option) {
      state.optionList.forEach((elem) => {
        if (elem.type === option.type) {
          elem.count += 1
        }
      })
    },
    OPTION_DECREASE(state, option) {
      state.optionList.forEach((elem) => {
        if (elem.type === option.type && elem.count) {
          elem.count -= 1
        }
      })
    },
  },
  actions: {
  },
  modules: {
  }
})