<template>
  <div class="youtubeplayer videoitem d-flex text-start" @click="selectVideo">
    <img :src="imgSrc" alt="video-thumbnail" class="imgitem">
    <div width="246px" height="90px">
      {{ videoTitle }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    videoItem: Object,
  },
  data() {
    return {
      imgSrc: this.videoItem.snippet.thumbnails.default.url,
      imgWidth: this.videoItem.snippet.thumbnails.default.width,
      imgHeight: this.videoItem.snippet.thumbnails.default.height,
      videoTitle: this.videoItem.snippet.title
    }
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.videoItem)
    }
  }
}
</script>

<style scoped>
  .videoitem{
    background-color: white;
    border: 1px solid rgb(201, 197, 197);
    padding: 8px 16px;
    width: 416px;
    height: 108px;
  }
  .videoitem:hover{
    background-color: #eee;
  }
  .imgitem{
     width: "120px";
     height: "90px";
     margin-right: 16px;
  }
</style>