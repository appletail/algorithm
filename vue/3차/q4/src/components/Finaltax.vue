<template>
  <div>
    <h2>결정세액: {{ taxCalculated - taxReduction > 0 ? taxCalculated - taxReduction : 0}} 만원</h2>
  </div>
</template>

<script>
export default {
  name:'Finaltax',
  props: {
    taxCalculated: Number,
    taxReduction: Number
  }
}
</script>

<style>

</style>