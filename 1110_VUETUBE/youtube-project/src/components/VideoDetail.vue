<template>
  <div v-if="video">
    <div>
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
    <div>
      {{ video?.snippet.title }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
}
</script>

<style>

</style>