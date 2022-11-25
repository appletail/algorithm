<template>
  <div @click="goDetail(article.id)">
    <p>글 번호 : {{ article.id }}</p>
    <p>제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      // 파라미터가 없는 경우 하는 방법
      // 바로 넣는 방식
      // this.$router.push({ name:'detail', params: {id : `${this.article.id}`} })
      // 변수로 따로 빼서하는 방식
      // const id = this.article.id
      this.$router.push({ name:'detail', params: {id} })

    }
  }
}
</script>

<style>

</style>