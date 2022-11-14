<template>
  <div>
    <h1>모든 할일</h1>
    <TodoInputForm
      :isImportant="false"
    />
    <hr>
    <TodoListItem
      v-for="todo in todos"
      :key="todo.id"
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoInputForm from '@/components/TodoInputForm'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'AllTodoPage',
  components: {
    TodoInputForm,
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todo.list
    },
  }
}
</script>

<style>

</style>