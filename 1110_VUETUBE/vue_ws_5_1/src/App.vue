<template>
  <div id="app box">
    <h1 style="text-align:center">Coffee Order App</h1>
    <MenuList class="left"/>
    <SizeList class="right"/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'

export default {
  name: 'App',
  components: {
    MenuList, SizeList,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

.left {
  flex-grow: 1;
  float: left;
  width: 50%;
}
.right {
  flex-grow: 1;
  float: right;
  width: 50%;  
}
/* #app {
  width: 100%;
  height: 100px;
  border: 1px solid #003458;
  background-color: lightgrey;
} */
</style>
