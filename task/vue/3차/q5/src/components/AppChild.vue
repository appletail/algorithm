<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model.number="childData" @input="childToParent">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name:'AppChild',
  data: function () {
    return {
      childData: null,
    }
  },
  props: {
    appData: Number,
    parentData: Number
  },
  methods: {
    childToParent: function () {
      this.$emit('child-data', this.childData)
    }
  }
}
</script>

<style>

</style>