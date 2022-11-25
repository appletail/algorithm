<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: '로딩중...',
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method: 'get',
        url: dogImageUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          this.$router.push('/404')
          console.log(error)
          // this.message = `${this.$route.params.breed}는 없는 페이지입니다.`
        })
    }
  },
  created() {
    this.getDogImage()
  }
}
</script>

<style>

</style>