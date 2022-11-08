<template>
  <div 
    @click="selectSize"
    class="items pa-2 ma-1 rounded-xl"
    :class="{ 'selected-item': size.selected }"
  >
    <div 
      style="min-height: 45px;"
      class="d-flex justify-space-between align-center"
    >
      <span>{{ size.name }}</span>
      <span>{{ size.price }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    selectSize() {
      this.$store.commit('updateSizeList', this.size)
    }
  }
}
</script>

<style>
</style>