<template>
  <div>
    <h2>산출세액 : {{ taxCalculated }} 만원</h2>
    <h2>세액감면 : (-) {{ taxReduction }} 만원</h2>
    <hr>
    <Finaltax
      :tax-calculated="taxCalculated"
      :tax-reduction="taxReduction"
    />
  </div>
</template>

<script>
import Finaltax from '@/components/Finaltax'

export default {
  name: 'Taxrate.vue',
  components: {
    Finaltax,
  },
  props: {
    taxBase: Number,
    taxReduction: Number,
  },
  computed: {
    taxCalculated: function () {
      let tmp = this.taxBase
      if (this.taxBase <= 1200) {
        tmp *= 0.06
        tmp = Math.round(tmp)
      } else if (this.taxBase <= 4600) {
        tmp *= 0.15
        tmp = Math.round(tmp) - 108
      } else if (this.taxBase <= 8800) {
        tmp *= 0.24
        tmp = Math.round(tmp) - 522
      } else if (this.taxBase <= 15000) {
        tmp *= 0.35
        tmp = Math.round(tmp) - 1490
      } else if (this.taxBase <= 30000) {
        tmp *= 0.38
        tmp = Math.round(tmp) - 1940
      } else if (this.taxBase <= 50000) {
        tmp *= 0.40
        tmp = Math.round(tmp) - 2540
      } else if (this.taxBase <= 100000) {
        tmp *= 0.42
        tmp = Math.round(tmp) - 3540
      } else {
        tmp *= 0.45
        tmp = Math.round(tmp) - 6540
      }
      return tmp
    }
  }
}
</script>

<style>

</style>