<template>
  <div>
    <h1>Home or About</h1>
    <h2>첫 번째 박스</h2>
    <div class="global box1">
      <div class="box scoped-box" id="test"></div>
    </div>
    <h2>두 번째 박스</h2>
    <div class="global box1">
      <div class="box scoped-box" id="test"></div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
/* * {
  color: #fa8;
} */
.box1 {
  background-color: #fa8;
}
</style>