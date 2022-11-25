<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <label for="Id">ID</label>
      <input type="text" id="Id" v-model="username"><br>
      <label for="password">password</label>
      <input type="password" id="password" v-model="password">
      <button>로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/token/',
        data: {
          username: this.username,
          password: this.password,
        }
      })
        .then((res) => {
          localStorage.setItem('jwt', res.data.access)
          this.$emit('login', true)
          this.$router.push({ name: 'TodoList' })
        })
        .catch(() => {
          alert('잘못입력')
        })
    }
  }
}
</script>
