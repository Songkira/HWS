<template>
  <div id="app">
    <nav class="nav justify-content-end">
      <router-link :to="{ name: 'MovieView' }">Movie</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'RandomView' }">Random</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'WatchListView' }">WatchList</router-link>
    </nav>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    this.$store.dispatch('movieGet')
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: #1f242a;
}

nav a {
  font-weight: bold;
  color: white;
  word-spacing: 20px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
nav router-link {
  padding: 0px 20px;
}
</style>
