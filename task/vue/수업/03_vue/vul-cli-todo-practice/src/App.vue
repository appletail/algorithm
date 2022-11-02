<template>
  <div id="app">
    <TodoForm @create-todo='createTodo'/>
    <TodoList
      :todos='todos'
      @delete-todo='deleteTodo'
    />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: []
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
      // this.todos.push({title: todoTitle})
    },
    deleteTodo: function (todo) {
      const index = this.todos.indexOf(todo)
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style>

</style>
