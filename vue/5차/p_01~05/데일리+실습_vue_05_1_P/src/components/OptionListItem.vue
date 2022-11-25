<template>
  <div 
    id="option"
    class="option-list d-flex justify-space-between 
           pa-2 ma-1 rounded-xl align-center"
    >
    <div>
      {{ option.type }}
    </div>
    <div style="min-height: 45px;" class="d-flex align-center ">
      <div class="text-center" @click="decrease">
        <v-btn
          class="mx-2"
          elevation="5"
          icon
          small
          color="primary"
        >
          <v-icon>
            mdi-minus
          </v-icon>
        </v-btn>
      </div>
      <span>{{ option.count }}</span>
      <div class="text-center" @click="increase">
        <v-btn
          class="mx-2"
          elevation="5"
          icon
          small
          color="primary"
        >
          <v-icon>
            mdi-plus
          </v-icon>
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.commit('OPTION_INCREASE', this.option)
    },
    decrease() {
      this.$store.commit('OPTION_DECREASE', this.option)
    },
  },
}
</script>

<style>
.option-list{
  border: solid 2px;
  border-color: black;
  transition: background-color 0.4s, color 0.4s;
}
</style>