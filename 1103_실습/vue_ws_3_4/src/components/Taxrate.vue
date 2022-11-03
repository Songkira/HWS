<template>
  <div>
    <h2>산출세액 : {{ taxBaseConfirm }} 만원</h2>
    <h2>세액감면 : (-) {{ taxMinus }} 만원</h2>
    <hr>
    <Finaltax
    :confirm-tax="taxBaseConfirm"
    :base-tax="baseTax"
    :tax-minus="taxMinus"/>
  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax'

export default {
  name: 'taxRate',
  components: {
    Finaltax,
  },
  props: {
    baseTax: Number,    // 과세표준
    taxMinus: Number,   // 세액감면액
  },
  data: function() {
    return {
      calculatedTax: '',
    }
  },
  methods: {
  }, 
  computed: {
    taxBaseConfirm() {
      if (this.baseTax <= 1200) {
        return Math.round(this.baseTax * 0.06)
      } else if (1200 < this.baseTax <= 4600) {
        return Math.round(this.baseTax * 0.15) -108
      } else if (4600 < this.baseTax <= 8800) {
        return Math.round(this.baseTax * 0.24) -522
      } else if (8800 < this.baseTax <= 15000) {
        return Math.round(this.baseTax * 0.35) -1490
      } else if (15000 < this.baseTax <= 30000) {
        return Math.round(this.baseTax * 0.38) -1940
      } else if (30000 < this.baseTax <= 50000) {
        return Math.round(this.baseTax * 0.4) -2540
      } else if (50000 < this.baseTax <= 100000) {
        return Math.round(this.baseTax * 0.42) -3540
      } else if (this.baseTax < 100000) {
        return Math.round(this.baseTax * 0.45) -6540
      } else {
        return 0
      }
    },

  },
}
</script>

<style>

</style>