<template>
  <div id="app">
    <header>
      <h1>Toutobe Project</h1>
      <TheSearchBar
      @input-change="inputChange"
      />
    </header>
    <section>
      <VideoDetail :video="selectedVideo"/>
      <VideoList :videos="videos" @select-video="selectVideo"/>
    </section>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

// 서버 재시작해서 key 확인
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// console.log(API_KEY)

export default {
  name: 'App',
  components: {
    TheSearchBar, VideoList, VideoDetail,
  },
  data() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    selectVideo(video) {
      console.log(video.snippet.title)
      this.selectedVideo = video
    },
    inputChange(query) {
      console.log('App>>', query)
      axios({
        url: 'https://www.googleapis.com/youtube/v3/search',
        method: 'get', // method는 필수는 아님
        params: {
          key: API_KEY,
          part: 'snippet',
          q: query, // 검색어
          type: 'video',
        },
      })
      .then(res => {
        console.log(res)
        this.videos = res.data.items
      })
      .catch(err => console.log(err))
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
section {
  display: flex;
}
</style>
