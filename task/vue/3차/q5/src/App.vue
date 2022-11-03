<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model.number="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <hr>
    <AppParent
      :app-data="appData"
      @parent-data="childsData"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data: function () {
    return {
      appData: null,
      childData: null,
      parentData: null,
    }
  },
  methods: {
    childsData: function (cData, pData) {
      this.childData = cData
      this.parentData = pData
    }
  }
}
</script>

<style>

</style>
