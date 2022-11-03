<template>
  <li class="list-group-item" @click="selectVideo">
    <img :src="thumbnailUrl">
    {{ videoTitle }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideo() {
      // console.log('click')
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    videoTitle() {
      return _.unescape(this.video.snippet.title)
    },
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>

</style>