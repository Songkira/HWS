// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  methods: {
    increase: function () {
      // const newNumber = this.counter
      this.$store.dispatch('increase')
      // this.counter += 1
    },
    decrease: function () {
      // const newNumber2 = this.counter
      this.$store.dispatch('decrease')
      // this.counter -= 1
    },
  },
  computed: {
    counter() {
      return this.$store.state.counter
    },
    counterDouble: function () {
      return this.$store.getters.counterDouble
    },
  },
}
</script>

<style>
</style>