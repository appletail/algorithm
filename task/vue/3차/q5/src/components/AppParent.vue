<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model.number="parentData">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <hr>
    <AppChild
      :parent-data="parentData"
      :app-data="appData"
      @child-data="parentToApp"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  
  name:'AppParent',
  data: function () {
    return {
      parentData: null,
      childData: null
    }
  },
  components:{
    AppChild,
  },
  props: {
    appData: Number
  },
  methods: {
    parentToApp: function (cData) {
      this.childData = cData
      this.$emit('parent-data', cData, this.parentData)
    }
  }
}
</script>

<style>

</style>