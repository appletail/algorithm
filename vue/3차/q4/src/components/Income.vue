<template>
  <div>
    <div>
      <label for="salary">연봉 입력 (만원): </label>
      <input type="number" id="salary" v-model.number="salary">
      <br>
      <label for="tax-reduction">세액감면액 (만원): </label>
      <input type="number" id="tax-reduction" v-model.number="taxReduction">
      <hr>
      <h2>종합소득금액 : {{ salary }} 만원</h2>
      <h2>종합소득공제 : (-) 150 만원</h2>
      <h2>과세표준 : {{ taxBase }} 만원</h2>
    </div>
    <hr>
    <Taxrate 
      :tax-base='taxBase'
      :tax-reduction='taxReduction'
    />
  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate'

export default {
  name: 'Income',
  components: {
    Taxrate
  },
  data: function () {
    return {
      salary: 0,
      taxReduction: 0,
    }
  },
  computed: {
    taxBase: function () {
      return this.salary - 150 > 0 ? this.salary - 150 : 0
    }
  }

}
</script>

<style>

</style>