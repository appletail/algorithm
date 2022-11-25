<template>
  <div>
    <input
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      // this.$store.dispatch('액션 메서드 이름')
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>