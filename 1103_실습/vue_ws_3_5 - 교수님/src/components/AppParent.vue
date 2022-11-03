<template>
  <div class="red">
    <h1>AppParent</h1>
    <!-- <input type="text" @input="inputChange(1, $event)"> -->
    <input type="text" @input="inputChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild 
    :app-data="appData"
    :parent-data="parentData"
    :child-data="childData"
    @child-input="childInput"/>

  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild
  },
  props: {
    appData: String,
    parentData: String,
    childData: String,
    // type: Number, Boolean, String, Array, Object, Function, Promise
  },
  methods: {
    childInput(childData) {
      this.$emit('child-input', childData)
    },
    inputChange(event) {
      this.$emit('parent-input', event.target.value)
    }
  }
}
</script>

<style>
  .red {
    border: 1px solid crimson;
  }
</style>