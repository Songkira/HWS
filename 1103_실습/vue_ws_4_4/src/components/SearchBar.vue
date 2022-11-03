<template>
  <div>
    <input type="text"
      v-model.trim="query"
      @keyup.enter="onInputChange"
    >
    <button class="btn btn-primary">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      query: '',
    }
  },  
  methods : {
    onInputChange() {
      if(!this.query) return
      // console.log(this.query)
      this.$emit('input-change', this.query)
      this.query = ''
    }
  }
}
</script>

<style>

</style>