<template>
  <div class="block">
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <button 
      :class="teacherSelected.Eric"
      @click="teacherClicked('Eric')"
    >Eric</button>
    <button 
      :class="teacherSelected.Tony"
      @click="teacherClicked('Tony')"
    >Tony</button>
    <hr>
    <div>
      <h3>시간 선택</h3>
      <button 
        v-for="(time, idx) in times" :key="idx"
        :class="isSelect[idx]"
        @click="timeClicked(idx)"
      >{{ time }}
      </button>
      <button @click="confirm" :class="'teacherUnselected'">예약 확정</button>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'TimeTable',
  data: function () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      teacherSelected: {
        Eric: 'teacherUnselected',
        Tony: 'teacherUnselected',
      },
      teacher: '',
      timeSelecteds: [],
      isSelect: Array.from({length: 18}, () => 'unselected')
    }
  },
  methods: {
    timeClicked: function (idx) {
      if (this.isSelect[idx] === 'selected') {
        // this.isSelect[idx] = 'unselected'
        const index = this.timeSelecteds.indexOf(this.times[idx])
        this.timeSelecteds.splice(index, 1)
        let arr = [...this.isSelect]
        arr[idx] = 'unselected'
        this.isSelect = arr
      } else {
        if (this.timeSelecteds.length >= 5) {
          window.alert('5타임까지만 신청할 수 있습니다.')
        } else {
          // this.isSelect[idx] = 'selected'
          this.timeSelecteds.push(this.times[idx])
          this.timeSelecteds.sort()
          let arr = [...this.isSelect]
          arr[idx] = 'selected'
          this.isSelect = arr
        }
      }
    },
    teacherClicked: function (name) {
      if (name === 'Eric') {
        this.teacherSelected.Eric = 'teacherSelected'
        this.teacherSelected.Tony = 'teacherUnselected'
        this.teacher = name
      } else {
        this.teacherSelected.Tony = 'teacherSelected'
        this.teacherSelected.Eric = 'teacherUnselected'
        this.teacher = name
      }
    },
    confirm: function () {
      if (!this.teacher) {
        window.alert('선생님을 선택해 주세요!')
      } else if (!this.timeSelecteds.length) {
        window.alert('시간을 선택해 주세요!')
      } else {
        const times = this.timeSelecteds
        this.$emit('teacher-and-times', this.teacher, times)
        this.teacherSelected.Eric = 'teacherUnselected'
        this.teacherSelected.Tony = 'teacherUnselected'
        this.timeSelecteds = []
        this.teacher = ''
        this.isSelect = Array.from({length: 18}, () => 'unselected')
      }
    }
  },
}
</script>

<style>
.unselected {
  color: #84898C;
  background-color: white;
  border: 0;
}
.selected {
  color: #0f4c81;
  background-color: #658dc63d;
  border: 0;
}
.teacherUnselected{
  color: #424242;
  background-color: white;
  border-color: #0f4c81;
  margin: 5px;
}
.teacherSelected{
  color: #424242;
  background-color: #658dc63d;
  border-color: #0f4c81;
  margin: 5px;
}
.block{
  color: #424242;
  display: inline-block;
  width: 450px;
}
hr{
  background: #0f4c81;
  height: 1px;
  border: 0;
}
</style>