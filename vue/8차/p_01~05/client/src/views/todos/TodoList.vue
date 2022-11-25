<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span
          @click="updateTodoStatus(todo)"
          :class="{ 'is-completed': todo.is_completed }"
        >
          {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from "axios";

const token = localStorage.getItem('jwt')

export default {
  name: "TodoList",
  data: function () {
    return {
      todos: null,
    };
  },
  methods: {
    getTodos: function () {

      axios({
        method: "get",
        url: "http://127.0.0.1:8000/todos/",
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          this.todos = res.data;
        })
        .catch(() => {
          alert('세션이 만료되었습니다. 다시 로그인해 주세요.')
          this.$router.push({ name: 'Logout' })
        });
    },
    deleteTodo: function (todo) {
      // 3번 문제
      axios({
        method: "DELETE",
        url: `http://127.0.0.1:8000/todos/${todo.id}`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res);
          this.getTodos();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateTodoStatus: function (todo) {
      // 4번 문제
      todo.is_completed = !todo.is_completed;
      axios({
        method: "PUT",
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          id: todo.id,
          title: todo.title,
          is_completed: todo.is_completed,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getTodos();
  },
};
</script>

<style scoped>
.todo-btn {
  margin-left: 10px;
}

.is-completed {
  text-decoration: line-through;
  color: rgb(112, 112, 112);
}
</style>
