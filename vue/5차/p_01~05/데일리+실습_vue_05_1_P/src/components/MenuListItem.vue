<template>
  <div 
    @click="selectMenu" 
    id="menu"
    class="items d-flex justify-space-between 
           pa-2 ma-1 rounded-xl align-center"
    :class="{ 'selected-item': menu.selected }"
    >
    <img :src="menu.image" :alt="menu.title" class="rounded-lg">
    <span>{{ menu.title }}</span>
    <span>{{ menu.price }}</span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    selectMenu() {
      this.$store.commit('updateMenuList', this.menu)
    }
  }
}
</script>

<style>
  img{
    width: 45px;
    height: 45px;
  }
</style>