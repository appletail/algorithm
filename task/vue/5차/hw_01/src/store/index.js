import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    counterDouble(state) {
      return state.counter * 2
    },
  },
  mutations: {
    increase(state) {
      state.counter += 1
    },
    decrease(state) {
      state.counter -= 1
    },
  },
  actions: {
  },
  modules: {
  }
})
