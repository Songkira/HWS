<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="food_random">Pick Lunch</button>
    <p>{{ menu }}</p>

    <h2>로또를 뽑아보자</h2>
    <button @click="toLotto">Pick Lotto</button>
  </div>
</template>

<script>

export default {
  name: 'LunchView',
  data() {
    return {
      menu : '',
    }
  },  
  methods: {
    toLotto() {
      this.$router.push({name: 'lotto'})
    },
    food_random() {
          const menu_lst = ['돼지국밥', '떡볶이', '치킨', '국수', '아구찜']
          const pick = Math.floor(Math.random() * 4 + 1)
          this.menu = menu_lst[pick]
    },
  }
}
</script>

<style>

</style>