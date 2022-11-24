<template>
  <div>
    <h4>Login</h4>
    <form @submit.prevent="login">
      <label for="username">username:</label>
      <input type="text" id="username" v-model="username" required> <br>
      
      <label for="password">password:</label>
      <input type="password" id="password" v-model="password"> <br>

      <input type="submit">

    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const payload = {
        username: this.username,
        password: this.password,
      }
      this.$store.dispatch('login', payload)
    }
  },
}
</script>

<style>

</style>