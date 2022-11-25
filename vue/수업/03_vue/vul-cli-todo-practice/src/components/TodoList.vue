<template>
  <div>
    <h1>TodoList</h1>
    <ul v-for='(todo, idx) in todos' :key='`todo-${idx}`'>
      <TodoListItem
        :todo='todo'
        @delete-todo='deleteTodo'
      />
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  props: {
    todos: Array,
  },
  methods: {
    deleteTodo: function (todo) {
      this.$emit('delete-todo', todo)
    }
  }
}
</script>

<style>

</style>