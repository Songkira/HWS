<template>
  <div>
    <h1>할일 생성</h1>
    <input type="text" v-model.trim="todoTitle">
    <!-- <button @click="createTodo">+</button> -->
    <button @click="onInputChange">+</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'CreateTodo',
  data() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    // createTodo() {this.$store.dispatch('createTodo', this.todoTitle) }
    ...mapActions(['createTodo']),
    onInputChange() {
      if(!this.todoTitle) return
      this.createTodo(this.todoTitle)
    },
  },
}
</script>

<style>

</style>