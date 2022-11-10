<template>
  <div>
    <span 
      @click="updateTodoStatus(todo)"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus',
    ]),
    // deleteTodo() {
    //   // console.log('삭제 메서드 호출!!')
    //   this.$store.dispatch('deleteTodo', this.todo)
    //   // this.$store.commit('DELETE_TODO', this.todo)
    // },
    // updateTodoStatus() {
    //   this.$store.dispatch('updateTodoStatus', this.todo)
    // },
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>
