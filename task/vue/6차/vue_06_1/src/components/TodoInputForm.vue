<template>
  <div>
    <input type="text" placeholder="할 일을 작성해주세요!"
      v-model="todoInput"
      @keyup.enter="OnTodoInput"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoInputForm',
  props: {
    isImportant: Boolean,
  },
  data() {
    return {
      todoInput: null,
    }
  },
  methods: {
    OnTodoInput() {
      const todoInput = {
        isImportant: this.isImportant,
        input: this.todoInput
      }
      this.$store.dispatch('todo/OnTodoInput', todoInput)
      this.todoInput = null
    }
  }
}
</script>

<style>

</style>