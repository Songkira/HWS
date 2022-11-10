<template>
  <div class="box box1 "
    @click="updateMenuList"
    :class="{'selected' : menu.selected }">
    <span>
      <img src="" alt="">
      {{ menu.title }}
      {{ menu.price }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    updateMenuList() {
      this.$store.dispatch('updateMenuList', this.menu)
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