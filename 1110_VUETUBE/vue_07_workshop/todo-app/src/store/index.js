import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router/'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
  },
  getters: {
  },
  mutations: {
    SET_TODOS(state, todos) { state.todos = todos },
    CREATE_TODO(state, todo) { state.todos.push(todo) },
  },
  actions: {
    createTodo({commit}, todoTitle) {
      axios({
        url: 'http://127.0.0.1:8000/todos/',
        method: 'post',
        data: {
          title: todoTitle,
          is_completed: false,
        }
      })
        .then(res => {
          console.log(res)
          commit('CREATE_TODO', res.data)
          router.push({name: 'index'}) // router.push('/')
        })
    },
    getTodos({commit}) {
      axios({
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          console.log(res)
          commit('SET_TODOS', res.data)
        })
    }
  },
  modules: {
  }
})
