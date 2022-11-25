<template>
  <div>
    <h1>중요 할일</h1>
    <TodoInputForm
      :isImportant="true"
    />
    <hr>
    <div
      v-for="todo in todos"
      :key="todo.id"
    >
      <TodoListItem
        :todo="todo"
        v-if="todo.isImportant && !todo.isCompleted"
      />
    </div>
  </div>
</template>

<script>
import TodoInputForm from '@/components/TodoInputForm'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'ImportantTodoPage',
  components: {
    TodoInputForm,
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todo.list
    }
  }
}
</script>

<style>

</style>