<template>
  <div id="app">
    <h1>AppChild</h1>
    <input type="text"
    v-model="childNum"
    @change="childInput">
    <p>appData: {{ dynamicApps }}</p>
    <p>parentData: {{ dynamicAppParents }}</p>
    <p>childData: {{ childNum }}</p>
  </div>

</template>

<script>

export default {
  name: 'AppChild',
  data: function () {
    return {
      childNum: null,
    }
  },
  props: {
    dynamicApps: String,
    dynamicAppParents: String,
  },
  methods: {
    childInput: function (event) {
      this.$emit('child-parent', this.childNum)
      this.childNum = event.target.value
    }
  }
}
</script>

<style>

</style>