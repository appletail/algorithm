<template>
  <div>
    <h1>오늘 할일</h1>
    <TodoInputForm
      :isImportant="false"
    />
    <hr>
    <div
      v-for="todo in todos"
      :key="todo.id"
    >
      <TodoListItem
        :todo="todo"
        v-if="dueCheck(todo) && !todo.isCompleted"
      />
    </div>
  </div>
</template>

<script>
import TodoInputForm from '@/components/TodoInputForm'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodayTodoPage',
    components: {
    TodoInputForm,
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todo.list
    },
  },
  methods: {
    dueCheck(todo) {
      if (todo.dueDateTime.getFullYear() === new Date().getFullYear()
      && todo.dueDateTime.getMonth() === new Date().getMonth()
      && todo.dueDateTime.getDate() === new Date().getDate()
      ) { return true } else { return false }
    }
    
  }
}
</script>

<style>

</style>