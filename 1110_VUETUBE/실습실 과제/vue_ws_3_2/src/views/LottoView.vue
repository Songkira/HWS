<template>
  <div>
    <h1>로또</h1>
    <button @click="rotto_random">Get Lucky Numbers</button>
    <p>{{ rotto }}</p>

    
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data() {
    return {
      rotto: [],
    }
  },
  methods: {
    rotto_random() {
      const numbers =  _.range(1, 46)
      const rotto = _.sampleSize(numbers, 6)
      this.rotto = rotto
    },
  },
}
</script>

<style>

</style>