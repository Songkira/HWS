<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import router from '@/router'
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo() {
      axios({
        url: `http://127.0.0.1:8000/todos/`,
        method: 'post',
        data: {
          title: this.title,
        },
      })
      .then(res => {
        console.log(res)
        router.push({ name: 'TodoList'})
      })
      .catch(err => console.log(err))
    },
  },
}
</script>
