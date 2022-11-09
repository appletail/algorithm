<template>
  <div>
    <div>
      <h2>시작</h2>
      <div>
        <router-link :to="{ name: 'home' }"><button>&lt;</button></router-link>
        <img src="@/assets/happeed.png" alt="" style="width: 480px; height: 450px">
        <router-link :to="{ name: 'happling' }"><button>&gt;</button></router-link>
      </div>
      <h2>해피드</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NocolorView',
}
</script>

<style>

</style>