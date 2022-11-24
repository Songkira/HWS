import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    randommovie: '',
    watchesList: [],
  },
  getters: {
    randomMovie(state) { return _.sample(state.movies)}
  },
  mutations: {
    MOVIE_GET(state, data) {
      state.movies = data
    },
    CREATE_WATCH(state, data) {
      state.watchesList.push(data)
    },
    UPDATE_WATCH(state, data) {
      state.watchesList = state.watchesList.map((watch) => {
        if (watch === data) {
          watch.selected = !watch.selected
        }
        return watch
      })
    }
  },
  actions: {
    movieGet({commit}) {
      axios({
        url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=ca158273547c25b0e40e27f43a977c06&language=ko-KR&page=1',
        method: 'get',
      })
        .then(res => {
          commit('MOVIE_GET', res.data.results)
        })
        .catch(err => console.log(err))
    },
    createWatch(context, watchList) {
      const watches = {
        title: watchList,
        selected: false,
      }
      context.commit('CREATE_WATCH', watches)
    },
    updateWatch(context, watch) {
      context.commit('UPDATE_WATCH', watch)
    }
  },
  modules: {
  }
})
