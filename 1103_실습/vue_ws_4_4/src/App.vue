<template>
  <div id="app">
    <div class="container">
      <h1>SSAFY TUBE</h1>
      <SearchBar 
      @input-change="inputChange"/>
      <div class="row">
        <div class="col-12 col-lg-8">
          <VideoDetail :selected-video="selectedVideo"/>
        </div>
        <div class="col-12 col-lg-4">
          <VideoList :videos="videos" @select-video="selectVideo"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar' 
import VideoList from '@/components/VideoList' 
import VideoDetail from '@/components/VideoDetail' 

const API_KEY = process.env.VUE_APP_YOUTUBE_KEY
// console.log(API_KEY)
export default {
  name: 'App',
  components: {
    SearchBar, 
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videos: [],
      selectedVideo: null,  // {}
    }
  },
  methods: {
    selectVideo(video) {
      // console.log(video.snippet.title)
      this.selectedVideo = video
    },
    inputChange(query) {
      // console.log(query)
      axios({
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: API_KEY,
          part: 'snippet',
          q: query,
          type: 'video',
        },
      })
        .then(res => {
          // console.log(res.data.items)
          this.videos = res.data.items
        })
        .catch(err => console.log(err))
    }
  },
}
</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
#app {
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
