<template>
  <div>
    <h1>할일 목록</h1>
    <button @click="getTodos">Get Todos</button>
    <hr>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
      </li>
    </ul>
  </div>
</template>

<script>
// import axios from 'axios'
import {mapActions, mapState} from 'vuex'

export default {
  name: 'TodoList',
  computed: {
    // todos() { return this.$store.state.todos }
    ...mapState(['todos'])
  },
  methods: {
    // getTodos() {this.$store.dispatch('getTodos')}
    ...mapActions(['getTodos'])
  },
  created() {
    this.getTodos()
  },
}
</script>

<style>

</style>