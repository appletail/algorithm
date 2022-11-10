<template>
  <div class="d-flex justify-content-center" style="margin: 20px;">
    <input type="text" v-model="searchWord" @keyup.enter="searchData" class="search-bar btn-primary">
    <button @click="searchData" class="btn btn-primary ms-2" style="height: 40px;">검색</button>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchWord: null
    }
  },
  methods: {
    searchData() {
      this.$emit('search-data', this.searchWord)
    }
  },
}
</script>

<style scoped>
  .search-bar{
    width: 622px;
    height: 40px;
    border: 1px solid #0d6efd;
    border-radius: 4px;
    outline: none;
  }
</style>