<template>
  <div @click="goDetail(article.id)">
  <!-- <div @click="goDetail()"> -->
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
    // goDetail() {
      this.$router.push({ name: 'detail', params:{id}})
      // this.$router.push({ name: 'detail', params:{id: `${this.article.id}`}})
    }
  },
}
</script>

<style>

</style>