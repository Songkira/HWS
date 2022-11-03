<template>
  <div>
    <h2>결정세액: {{ totalTax }} 만원</h2>
  </div>  
</template>

<script>
export default {
  name: 'finalTax',
  props: {
    confirmTax: Number,
    baseTax: Number,
    taxMinus: Number,
  },
  computed: {
    totalTax() {
      if (this.confirmTax - this.taxMinus <= 0){
        return 0
      } else {
        return this.confirmTax - this.taxMinus
      }
    }
  }
}
</script>

<style>

</style>