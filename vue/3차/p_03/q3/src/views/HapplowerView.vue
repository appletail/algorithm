<template>
  <div>
    <div>
      <h2>시작</h2>
      <div>
        <router-link :to="{ name: 'happlossome' }"><button>&lt;</button></router-link>
        <img src="@/assets/happlower.png" alt="" style="width: 480px; height: 450px">
        <router-link :to="{ name: 'home' }"><button>&gt;</button></router-link>
      </div>
      <h2>해플라워</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HapplowerView',
}
</script>

<style>

</style>