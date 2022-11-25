<template>
  <div class="my-2">
    <div class="d-flex justify-space-between">
      <div class="d-flex align-center">
        <img :src="order.menu.image" :alt="order.menu.title" style="display: inline-block;" class="rounded-lg mr-3">
        <div style="display: inline-block;">
          <span>
            <div>{{ order.menu.title }}</div>
            <div>사이즈: {{ order.size.name }}</div>
          </span>
        </div>
      </div>
      <div>
        <div>가격: {{ totalPrice }}</div>
        <div>샷: {{ order.optionList[0].count }}회 | 바닐라 시럽: {{ order.optionList[1].count }}회 | 카라멜 시럽: {{ order.optionList[2].count }}회 |</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice() {
      const options = this.order.optionList.reduce((acc, cur) => {
        return acc + cur.price * cur.count
      }, 0)
      return this.order.menu.price + this.order.size.price + options
    },
  },
}
</script>

<style>
</style>