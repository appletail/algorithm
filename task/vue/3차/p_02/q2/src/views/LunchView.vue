<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ pick }}</p>


    <h2>로또를 뽑아보자</h2>
    <button>Pick Lotto</button>
    <input type="text" v-model="numbers" @keyup.enter="pickLotto">
  </div>
</template>

<script>
// @ is an alias to /src
import _ from 'lodash'

export default {
  name: 'LunchView',
  data() {
    return {
      lunch: ['국밥', '햄버거', '피자', '치킨', '짜장', '짬뽕', '육개장'],
      pick: null,
      numbers: null,
    }
  },
  methods: {
    pickLunch() {
      this.pick = this.lunch[_.random(0, this.lunch.length - 1, false)]
    },
    pickLotto() {
      this.$router.push({ name:'lotto', params: { numbers: this.numbers } })
    }
  }
}
</script>
