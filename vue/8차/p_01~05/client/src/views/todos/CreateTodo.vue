<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      // 2번 문제
      const token = localStorage.getItem('jwt')
      console.log(token)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          title: this.title,
        }
      })
        .then(() => {
          this.title = null
          this.$router.push({ name: 'TodoList' })
        })
        .catch((err) => {
          console.log(err)
          alert('다시 로그인해주세요')
        })
        
    }
  }
}
</script>
