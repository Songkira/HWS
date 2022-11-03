<template>
  <div id="app">
    <h1>AppParent</h1>
    <input type="text" 
    v-model="dynamicAppParents" 
    @change="ParentInput"
    >
    <p>appData: {{ dynamicApps }}</p>
    <p>childData: {{ childNum }}</p>
    <AppChild
    :dynamic-apps="dynamicApps"
    :dynamic-app-parents="dynamicAppParents"
    @child-parent="childData"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild,
  },
  props: {
    dynamicApps: String,
  },
  data: function() {
    return {
      dynamicAppParents: '',
      // dynamicApps: '',
      childNum: '',
    }
  },
  methods: {
    childData: function (childNum) {
      this.childNum = childNum
      this.$emit('child-app', childNum)
    },
    ParentInput: function () {
      this.$emit('parent-app', this.dynamicAppParents)
    },
  }
}
</script>

<style>

</style>
