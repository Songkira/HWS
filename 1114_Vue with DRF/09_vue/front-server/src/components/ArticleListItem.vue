<template>
  <div>
    <!-- <h5>PK</h5> -->
    <h5>{{ article.id }}</h5>
    <!-- <p>제목</p> -->
    <p>{{ article.title }}</p>
    <router-link 
    :to="{name: 'DetailView',params: { id : article.id }}">[DETAIL]
    </router-link>
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
