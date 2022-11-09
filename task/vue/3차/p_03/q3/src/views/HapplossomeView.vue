<template>
  <div>
    <div>
      <h2>시작</h2>
      <div>
        <router-link :to="{ name: 'happling' }"><button>&lt;</button></router-link>
        <img src="@/assets/happlossome.png" alt="" style="width: 480px; height: 450px">
        <router-link :to="{ name: 'happlower' }"><button>&gt;</button></router-link>
      </div>
      <h2>해플라썸</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HapplossomeView',
}
</script>

<style>

</style>