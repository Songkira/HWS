<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="dynamicApps" >
    <p>parentData: {{ parentNum }}</p>
    <p>childData: {{ childNum }}</p>
    <AppParent 
    :dynamic-apps="dynamicApps"
    @parent-app="parentData"
    @child-app="childData"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent,
  }, 
  props: {
    
  },
  data: function() {
    return {
      dynamicApps: '',
      parentNum: '',
      childNum: '',
    }
  },
  methods: {
    parentData: function (parentNum) {
      this.parentNum = parentNum
    },
    childData: function (childNum) {
      this.childNum = childNum
    }
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
  margin-top: 60px;
}
</style>
