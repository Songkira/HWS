<template>
  <div class="box box1 " @click="updateSizeList"
      :class="{'selected' : size.selected }">
    <span>
      {{ size.name }}
      {{ size.price }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    updateSizeList() {
      this.$store.dispatch('updateSizeList', this.size)
    }
  },
}
</script>
  
<style>
  .box1 {
    margin: 1px;
    border: 1px solid black;  
    border-radius: 5px;
    padding: 1px;
  }
  .selected {
    background-color: green;
  }
</style>