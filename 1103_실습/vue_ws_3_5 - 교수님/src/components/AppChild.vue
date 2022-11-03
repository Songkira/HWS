<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" @input="inputChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>


export default {
  name: 'AppChild',
  props: {
    appData: String,
    parentData: String,
    childData: String,
  },
  methods: {
    inputChange(event) {
      this.$emit('child-input', event.target.value)
    }
  }
}
</script>

<style>
  div {
      border: 1px solid blue;
    }
</style>