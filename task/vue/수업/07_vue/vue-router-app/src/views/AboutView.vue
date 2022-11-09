<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }" >홈으로!</router-link>
    <button @click="toHome">홈으로!</button>
    <input type="text" @keyup.enter="toHello" v-model="hello">

  </div>
</template>

<script>
export default {
  name: 'AboutView',
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    toHello() {
      this.$router.push({ name: 'hello', params: { userName: this.hello } } )
    }
  },
  data() {
    return {
      hello: null
    }
  }
}
</script>

