<template>
  <v-app id="app">
    <div class="ma-10">
      <h1 class="d-flex justify-center ma-5">Coffee Order App</h1>
      <div>
        <v-row
          class="d-flex justify-space-around"
          cols="3" sm="3"
        >
          <MenuList
            class="d-flex flex-column justify-space-around"
          />
          <SizeList
            class="d-flex flex-column justify-space-around"
          />
          <OptionList
            class="d-flex flex-column justify-space-around"
          />
        </v-row>
      </div>
      <div class="d-flex justify-center ma-9">
        <v-btn
          class="text-center"
          color="blue"
          dark
          @click="addOrder"
          style="min-width: 60%; display: inline-block;"
        >
          장바구니 담기
        </v-btn>
      </div>
      <OrderList/>
      <hr>
    </div>
  </v-app>
  
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OptionList from '@/components/OptionList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
  methods: {
    addOrder() {
      this.$store.commit('addOrder')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
.items{
  border: solid 2px;
  border-color: black;
  transition: background-color 0.4s, color 0.4s;
}
.items:hover{
  background-color: rgba(100, 148, 237, 0.534);
  color: black;
  border: solid 2px;
  border-color: black;
}
.selected-item{
  background-color: cornflowerblue;
  color: white;
  border: solid 2px;
  border-color: black;
}
</style>
