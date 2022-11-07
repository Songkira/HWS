import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 1,
  },
  getters: {
    doubleCounter(state) {
      return state.counter * 2
    },
  },
  mutations: {
    INCREASE(state) {
      state.counter++
    },
    DECREASE(state) {
      state.counter-- 
    },
  },
  actions: {
    increase(context) {
      console.log(context)
      context.commit('INCREASE')
    },
    decrease(context) {
      console.log(context)
      context.commit('DECREASE')
    },
  },
  modules: {
  }
})
