import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?americano>'
      },
      {
        title: '카푸치노',
        price: 4500,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?americano>'
      },
      {
        title: '카페라떼',
        price: 4000,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?americano>'
      },
    ],
    sizeList: [
      {
        name: 'samll',
        price: 0,
        selected: false, // 초기값
      },
      {
        name: 'medium',
        price: 500,
        selected: false,
      },
      {
        name: 'large',
        price: 1000,
        selected: false,
      }
    ],
  },
  getters: {
  },
  mutations: {
    UPDATE_MENU_LIST(state, selectedMenu) {
      // state.sizeList.selected = selectedSize,
      state.menuList.map((menu) => {
        if (menu === selectedMenu) {
          menu.selected = !menu.selected
        }
        return menu
      })
    },
    UPDATE_SIZE_LIST(state, selectedSize) {
      // state.sizeList.selected = selectedSize,
      state.sizeList.map((size) => {
        if (size === selectedSize) {
          size.selected = !size.selected
        }
        return size
      })
    },
    // ADD_ORDER(state, addMenu, addSize) {
    //   state.orderList.push(addMenu)
    //   state.orderList.push(addSize)
    // },
  },
  actions: {
    // addOrder(context, addMenu, addSize) {
    //   context.commit('ADD_ORDER', addMenu)
    //   context.commit('ADD_ORDER', addSize)
    // },
    updateMenuList(context, selectedMenu) {
      context.commit('UPDATE_MENU_LIST', selectedMenu)
    },
    updateSizeList(context, selectedSize) {
      context.commit('UPDATE_SIZE_LIST', selectedSize)
    },
  },
  modules: {
  }
})
