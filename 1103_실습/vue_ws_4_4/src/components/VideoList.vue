<template>
  <ul class="list-group">
    <!-- {{ videos }} -->
    <VideoListItem 
      v-for="video in videos" :key="video.etag"
      :video="video"
      @select-video="selectVideo"  
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem' 

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    selectVideo(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>