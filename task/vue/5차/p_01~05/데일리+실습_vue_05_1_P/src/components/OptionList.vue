<template>
  <div class="d-flex justify-space-between">
    <h1>3. 옵션을 고르세요.</h1>
    <ul>
      <OptionListItem
        v-for="(option, idx) in optionList"
        :key="`option-${idx}`"
        :option="option"
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },
  },
  methods: {
    // increase: function () {
    // },
    // decrease: function () {
    // },
  },
}
</script>

<style>
</style>