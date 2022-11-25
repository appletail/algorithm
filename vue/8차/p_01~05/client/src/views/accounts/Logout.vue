<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'Logout',
  data () {
    return {
    }
  },
  methods: {
    logout() {
      if (localStorage.getItem('jwt_access')) {
        localStorage.removeItem('jwt_access')
      }
      this.$router.push({ name: 'Login' })
    }
  },
  created() {
    this.logout()
  }
}
</script>
