<template>
  <div id="app">
    <h1 style="color: rgb(0, 110, 255);"><b>SSAFY TUBE</b></h1>
    <SearchBar @search-data="searchData"/>
    <div class="d-flex justify-content-center">
      <div class="me-4" style="font-size: 20px;">
        <div v-if="!isSelected" class="d-flex flex-column justify-content-center align-items-center youtubeplayer" style="width: 856px; height: 468px">
          <img src="@/assets/noResult.png" alt="NoResult" style="width: 200px; height: 200px">
          <p>선택된 비디오가 없습니다!</p>
          <p>비디오를 검색하시거나 리스트에서 골라 주세요!</p>
        </div>
        <iframe v-show="isSelected" id="player" type="text/html" width="856" height="482"
        :src="`http://www.youtube.com/embed/${youtubeVideoId}`"
        frameborder="0"></iframe><br>
        <VideoDetail
          class="youtubeplayer"
          v-show="isSelected"
          :youtube-title="youtubeTitle"
          :youtube-description="youtubeDescription"
        />
      </div>
        <VideoList
          :youtube-data="youtubeData"
          @select-video="selectVideo"
        />
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList,
  },
  data() {
    return {
      youtubeData: null,
      youtubeVideoId: null,
      youtubeTitle: null,
      youtubeDescription: null,
      youtubeSearch: 'ssafy',
      isSelected: false,
    }
  },
  methods: {
    youtube() {
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.youtubeSearch,
        }
      })
        .then((response) => {
          this.youtubeData = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    searchData(inputData) {
      this.youtubeSearch = inputData
      this.youtube()
    },
    selectVideo(videoItem) {
      this.youtubeVideoId = videoItem.id.videoId
      this.youtubeTitle = videoItem.snippet.title
      this.youtubeDescription = videoItem.snippet.description
      this.isSelected = true
    }
  },
  computed: {
    
  },
  created() {
    this.youtube()
  },
}
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 16px;
}
.youtubeplayer{
  box-shadow: inset 0 1px 1px 0 hsl(0deg 0% 100% / 10%), 0 50px 100px -20px rgb(50 50 93 / 25%), 0 30px 60px -30px rgb(0 0 0 / 30%);
}
</style>
