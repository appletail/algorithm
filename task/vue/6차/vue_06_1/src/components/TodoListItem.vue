<template>
  <div>
    <div class="todo-item">
      <div>
        <input type="checkbox" name="todo" :id="todo.id" 
          :checked="todo.isCompleted"
          @input="OnIsCompleted"
        >
        <div class="todo-content">{{ todo.content }}</div>
      </div>
        <input type="checkbox" name="todo" :id="todo.id" 
          :checked="todo.isImportant"
          @input="OnIsImportant"
        >
    </div>
    <TodoUpdateForm
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoUpdateForm from '@/components/TodoUpdateForm'

export default {
  name: 'TodoListItem',
  components: {
    TodoUpdateForm,
  },
  props: {
    todo: Object,
  },
  methods: {
    OnIsCompleted() {
      this.$store.dispatch('todo/OnIsCompleted', this.todo)
    },
    OnIsImportant() {
      this.$store.dispatch('todo/OnIsImportant', this.todo)
    }
  }
}
</script>

<style scoped>
  .todo-item{
    display: flex;
    justify-content: space-between;
  }
  .todo-content{
    display: inline-block;
    margin-left: 1rem;
  }

</style>