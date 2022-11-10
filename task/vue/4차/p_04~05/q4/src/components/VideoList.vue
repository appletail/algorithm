<template>
  <div>
    <VideoListItem
      v-for="videoItem in youtubeData.items"
      :key="videoItem.etag"
      :video-item="videoItem"
      @select-video="selectVideo"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    youtubeData: Object,
  },
  methods: {
    selectVideo(videoItem) {
      this.$emit('select-video', videoItem)
    },
  }
}
</script>

<style>

</style>