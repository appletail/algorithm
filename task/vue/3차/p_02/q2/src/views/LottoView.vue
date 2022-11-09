<template>
  <div class="lotto">
    <h1>로또</h1>
    <button @click="luckyNumbers">Get Lucky Numbers</button>
    <p>{{ sevenNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data() {
    return {
      sevenNumbers: null,
      numbers: this.$route.params.numbers
    }
  },
  methods: {
    luckyNumbers() {
      const tmpArr = []
      while (tmpArr.length < this.numbers) {
        const tmp = _.random(1, this.numbers)
        if (!tmpArr.includes(tmp)) {
          tmpArr.push(tmp)
        }
      }

      this.sevenNumbers = tmpArr
    }
  }
}
</script>

<style>

</style>