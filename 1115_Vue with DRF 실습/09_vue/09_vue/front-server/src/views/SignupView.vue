<template>
  <div>
    <h4>Signup</h4>
    <form @submit.prevent="signup">
      <label for="username">username:</label>
      <input type="text" id="username" v-model="username" required> <br>
      
      <label for="password1">password1:</label>
      <input type="password" id="password1" v-model="password1"> <br>

      <label for="password2">password2:</label>
      <input type="password" id="password2" v-model="password2"> <br>

      <input type="submit">

    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signup() {
      const payload = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
      }
      this.$store.dispatch('signup', payload)
    }
  }
}
</script>

<style>

</style>