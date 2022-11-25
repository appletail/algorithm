<template>
  <div class="border">
    <h1>내가 만든 쿠키~</h1>
    <!-- 부모에서 넘겨주는 props: kebab-case -->
    <!-- dynamic props는 v-bind로 보내기 -->
    <!-- 자식이 show-me-the-money라는 emit이벤트를 올렸을 때 동작 -->
    <MyComponentItem
      static-props='MyComponent에서 보낸 데이터'
      :my-props='dynamicProps'
      @show-me-the-money="parentGetEvent"
      @child-input="getDynamicData"
    />
    <!-- int 1을 보내기 위해서는 다이나믹 프롭스로 넘겨야함 스태틱으로 보내면 string 1이 보내짐 -->
  </div>
  
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
  // 다른 이름을 써도 되기는하지만 파일이름과 같은 것으로 써주는 것이 좋음
  name: 'MyComponent',

  // 하위 컴포넌트 등록
  components: {
    MyComponentItem,
  },
  data: function () {
    // vue cli에서는 함수의 return 객체로 써야한다
    // 만약 그냥 함수를 쓰지 않는다면 모든 컴포넌트에서 data를 공유해버림
    return {
      dynamicProps: '이건 동적인 데이터!'
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log(childData)
      console.log('용돈 없어!!')
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 '${childInputData}'입니다.`)
    }
  }

}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>