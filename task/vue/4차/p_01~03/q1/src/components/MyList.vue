<template>
  <div class="block" style="background-color: #658dc63d">
    <h2>상담 신청 현황</h2>
    <h3>상담 선생님</h3>
    <p>성함: {{teacherAndTimes.teacher}}</p>
    <hr>
    <h3>예약 현황</h3>
    <p>시간들 : <span v-for="(timeSelected, idx) in teacherAndTimes.times" :key="`$ts-${idx}`">{{ timeSelected }}  </span></p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MyList',
  props: {
    teacherAndTimes: Object,
  }
}
</script>

<style>

</style>