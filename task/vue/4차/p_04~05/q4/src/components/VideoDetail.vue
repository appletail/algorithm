<template>
  <div class="detail">
    <h4>{{ youtubeTitle }}</h4>
    <p>{{ trunc }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'VideoDetail',
  props: {
    youtubeTitle: String,
    youtubeDescription: String,
  },
  computed: {
    trunc() {
      return _.truncate(
        this.youtubeDescription, {
          'length': 55,
          'omission': '...'
        }
      );
    }
  }
}
</script>

<style scoped>
  .detail{
    width: 856px;
    border: 1px solid rgb(201, 197, 197);
  }
</style>