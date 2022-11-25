<template>
  <div>
    <h2>주문 내역</h2>
    <p>총 {{ totalOrderCount }}건: {{ totalOrderPrice }}원</p>

      <OrderListItem
        v-for="(order, idx) in orderList"
        :key="`order-${idx}`"
        :order="order"
      />
    
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    totalOrderCount() {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice() {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>