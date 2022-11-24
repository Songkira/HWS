import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    token: null,
    user: null,
    articles: [],
    article: {},
  },
  getters: {
    isAuthor: (state) => state.user?.username === state.article.username,
    article: (state) => state.article,
    articles: (state) => state.articles,
    isLogin: (state) => state.token? true: false,
    authHead: (state) => ({ Authorization: `Token ${state.token}` }), // 객체일때는 함수의 중괄호와 헷갈리기 때문에 가로 로 묶어줌
    user: (state) => state.user,

  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_USER: (state, user) => state.user = user,
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE: (state, article) => state.article = article,
  },
  actions: {
    getArtcileDetail({ commit }, articleId) {
      axios({
        url: `${API_URL}/api/v1/articles/${articleId}/`,
      })
      .then(res => {
        console.log(res)
        commit('SET_ARTICLE', res.data)
      })
      .catch(err => console.log(err))
    },
    getArticles({ commit }) {
      axios({
        url: `${API_URL}/api/v1/articles/`,
        // headers
      })
      .then(res => {
        console.log(res)
        commit('SET_ARTICLES', res.data)
      })
      .catch(err => console.log(err))
    },
    createArticle({ getters }, payload) {
      axios({
        url: `${API_URL}/api/v1/articles/`,
        method: 'post',
        data: {...payload},
        headers: getters.authHead,
      })
      .then(res => {
        console.log(res)
        router.push({ name: 'ArticleView' })
      })
      .catch(err => console.log(err))
    },
    signup({ commit }, payload) {
      axios({
        url:`${API_URL}/accounts/signup/`,
        method: 'post',
        data: {...payload},
      })
      .then(res => {
        console.log(res.data.key)
        commit('SET_TOKEN', res.data.key)
        router.push('/')
      })
      .catch(err => {
        console.log(err)
        if (err.response.status === 400) {
          alert(JSON.stringify(err.response.data))
        }
      })
    },
    login({ commit, dispatch }, { username, password }) {
      const payload = { username, password }
      axios({
        url:`${API_URL}/accounts/login/`,
        method: 'post',
        data: payload,
      })
      .then(res => {
        console.log(res.data.key)
        commit('SET_TOKEN', res.data.key)
        dispatch('getUserInfo')
        router.push({ name: 'ArticleView' })
      })
      .catch(err => {
        console.log(err)
        if (err.response.status === 400) {
          alert(JSON.stringify(err.response.data))
        }
      })
    },
    logout({ commit, getters }) {
      axios({
        url: `${API_URL}/accounts/logout/`,
        method: 'post',
        headers: getters.authHead,
      })
      .then(res => {
        console.log(res)
        commit('SET_TOKEN', null)
        commit('SET_USER', null)
      })
      .catch(err => console.log(err))
    },
    getUserInfo({ commit, getters }) {
      axios({
        url: `${API_URL}/accounts/user/`,
        method: 'get',
        headers: getters.authHead,
      })
        .then(res => {
          console.log(res)
          commit('SET_USER', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
