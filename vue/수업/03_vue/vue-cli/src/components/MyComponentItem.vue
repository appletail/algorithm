<template>
  <div>
  <h3>나는 MyComponent의 하위 컴포넌트</h3>
  <!-- 자식에서 받는 props: camelCase -->
  <p>{{ staticProps }}</p>
  <p>{{ myProps }}</p>
  <button @click="childToParent">불효!</button>
  <input 
    type="text" 
    v-model="childInputData"
    @keyup.enter="childInput"
  >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  // props에 선언을 해야 template에서 사용 가능
  props: {
    staticProps: String,
    myProps: String
  },
  data: function () {
    return {
        childInputData: null
      }
    },
  methods: {
    childToParent: function () {
      // 받는 곳이 html이기 때문에 kebab-case로 넘겨줘야함
      this.$emit('show-me-the-money', '응애 돈줘용 ㅎㅎ')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null
    },
  }
}
</script>

<style>

</style>