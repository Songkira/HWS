<template>
  <div>
    <p>PK: {{ article.id }}</p>
    <p>
      제목: 
      <router-link :to="{ name: 'DetailView', params: {id: article.id }}">
        {{ article.title }}
      </router-link></p>
      <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
}
</script>

<style>

</style>