<template>
  <div id="size">
    <h1>2. 사이즈를 고르세요.</h1>
      
    <SizeListItem
    v-for="size in sizeList"
    :key="size.title"
    :size="size"/>
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem.vue'

export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  methods: {
    onSelectMenu() {
      
    },
  },
  computed: {
    sizeList() {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
#size {
  border: 1px solid white;  
  border-radius: 5px;
  background-color: white;
}
</style>