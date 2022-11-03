<template>
  <div>
    <label for="year">연봉 입력 (만원): </label>
    <input type="number" v-model.number="year" name="name" id="name">
    <p>
      <label for="taxminus">세액감면액 (만원): </label>
      <input type="number" v-model.number="taxMinus" name="taxminus" id="taxminus">
    </p>
    <hr>
    <h2>종합소득금액 : {{ year }} 만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{ taxBase }} 만원</h2>
    <hr>
    <Taxrate 
    :base-tax="taxBase"
    :tax-minus="taxMinus"/>
  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate'

export default {
  name: 'inCome',
  data: function() {
    return {
      year: '',
      taxMinus: '',
    }
  },
  components: {
    Taxrate,
  },
  methods: {
    
  },
  computed: {
    taxBase() { // 과세표준
      if (this.year >= 150) {
        return this.year-150
      } else {
        return 0
      }
    },
  },
}
</script>

<style>

</style>