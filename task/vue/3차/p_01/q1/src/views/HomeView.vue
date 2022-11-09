<template>
  <div>
    <h1>Home</h1>
    <h2>첫 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
    <h2>두 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {

  }
}
</script>

<style>
  .box{
    height: 100px;
    width: 100px;
    border: solid 1px;
    display: inline-block;
  }

</style>