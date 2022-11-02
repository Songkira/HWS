<template>
   <div class="border"><!-- 컴포넌트를 구성하는 최상위 요소가 아무거나 있어야함 (보통 div Tag)  -->
    <h1>이거는 내가 만든 새로운 컴포넌트 다!</h1>
    <!-- 3. 사용하기 -->
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
      />

  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'
//  불러오고 나서 안쓰면 에러 뜸

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
    // 등록하고 안쓰면 도 에러 뜸
  },
  data: function() {
    return {
      dynamicProps: '이건 동적인 데이터',
    }
  },
  methods: {
    parentGetEvent: function(childData) {
      console.log('용돈 없어!!')
      console.log(childData)
    },
    getDynamicData: function(childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>