<template>
  <div id="app">
    <TimeTable
      style="display: inline-block"
      @teacher-and-times="teacherAndTimes"
    />
    <MyList
      style="display: inline-block"
      :teacher-and-times="toMyList"
    />
  </div>
</template>

<script>
import TimeTable from '@/components/TimeTable'
import MyList from '@/components/MyList'


export default {
  name: 'App',
  data: function () {
    return {
      toMyList:{
        teacher: '',
        times: [],
      }
    }
  },
  components: {
    TimeTable,
    MyList,
    
  },
  methods: {
    teacherAndTimes: function (teacher, times) {
      this.toMyList.teacher = teacher
      this.toMyList.times = times
    },
  }

}
</script>

<style>

</style>
