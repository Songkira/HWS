<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent 
    :app-data="appData"
    :parent-data="parentData"
    :child-data="childData"
    @parent-input="parentInput"
    @child-input="childInput"
    />

  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent
  },
  methods: {
    parentInput(inputData) {
      // console.log(inputData)
      this.parentData = inputData
    },
    childInput(inputData) {
      this.childData = inputData
    }
  },
  data: function() {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  border: 1px solid black;
}
</style>
