<template>
  <ul>

    <VideoListItem
      v-for="video in videos" :key=video.etag
      :video="video"
      @select-video="selectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: { VideoListItem },
  props: {
    videos: Array,
  },
  methods: {
    selectVideo(video) {
      // console.log('select-video', video)
      this.$emit('select-video', video)
    }
  },
}
</script>

<style>

</style>