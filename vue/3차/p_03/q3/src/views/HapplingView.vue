<template>
  <div>
    <div>
      <h2>시작</h2>
      <div>
        <router-link :to="{ name: 'happeed' }"><button>&lt;</button></router-link>
        <img src="@/assets/happling.png" alt="" style="width: 480px; height: 450px">
        <router-link :to="{ name: 'happlossome' }"><button>&gt;</button></router-link>
      </div>
      <h2>해플링</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HapplingView',
}
</script>

<style>

</style>