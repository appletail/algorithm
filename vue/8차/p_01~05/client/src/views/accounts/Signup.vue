<template>
  <div>
    <h1>회원가입</h1>
    <label for="username">ID</label>
    <input type="text" id="username" v-model="username"><br>
    <label for="password">password</label>
    <input type="password" id='password' v-model="password"><br>
    <label for="password_confirm">password_confirm</label>
    <input type="password" id='password_confirm' v-model="password_confirm">
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Singup',
  data () {
    return {
      username: null,
      password: null,
      password_confirm: null,
    }
  },
  methods: {
    signup () {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: this.username,
          password: this.password,
          password_confirm: this.password_confirm,
        }
      })
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>
