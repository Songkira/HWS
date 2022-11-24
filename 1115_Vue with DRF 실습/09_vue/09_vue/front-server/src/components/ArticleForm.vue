<template>
  <div>
    <form @submit.prevent="onSubmit">
      <label for="title">title:</label>
      <input type="text" v-model.trim="title"> <br>

      <label for="content">content</label>
      <input type="text" v-model.trim="content"> <br>

      <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'ArticleForm',
  props: {
    article: Object,
    action: String,
  },
  data() {
    return { 
      title: this.article.title , 
      content: this.article.content,
    }
  },
  methods: {
    createArticle() {
      const payload = { 
        title: this.title, 
        content: this.content 
      }
      this.$store.dispatch('createArticle', payload)
    },
    updateArticle() {

    },
    onSubmit() {
      if (this.action === 'create') {
        this.createArticle()
      } else {
        this.updateArticle()
      }
    }
  },
}
</script>

<style>

</style>