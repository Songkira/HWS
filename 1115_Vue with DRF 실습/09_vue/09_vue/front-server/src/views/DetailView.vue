<template>
  <div>
    <h4>DetailView</h4>
    <p>글번호: {{ article.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성자: {{ article.username }}</p>
    <hr>
    <div v-if="isAuthor">
      <router-link :to="{ name: 'UpdateView' }">UPDATE</router-link>
      <button>삭제하기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  created() {
    const articleId = this.$route.params.id
    this.$store.dispatch('getArtcileDetail', articleId)
  },
  computed: {
    article() { return this.$store.getters.article },
    isAuthor() { return this.$store.getters.isAuthor }
  },
}
</script>

<style>

</style>