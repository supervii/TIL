<template>
  <div class="movie-list">
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <!-- 2. 장르 선택(제일 마지막에 구현하시오.)
    2-1. App 컴포넌트로 부터 받은 genres를 반복하여 드롭다운을 완성 해주세요.
    2-2. 드롭다운은 selectedGenreId data와 양방향바인딩(v-model)이 됩니다.
    2-3. 값 변경이 되면, 특정한 함수를 실행 해야합니다.
     -->
    <select v-model="selectedGenreId" class="form-control">
      <option v-for="genre in genres" v-bind:key="genre.id" :value="genre.id">{{ genre.name }}</option>
    </select>

    <!-- 1-3. 반복을 통해 호출하시오. 
      필요한 경우 props를 데이터를 보내줍니다.
    -->
    <!-- (나중에 마지막으로) selectedGenreId 값에 따른 분기를 해야 합니다.-->
    <div class="row mt-5" v-if="selectedGenreId === 0">
      <movie-list-item v-for="movie in movies" :key="movie.id" :movie="movie"></movie-list-item>
    </div>
    <div class="row mt-5" v-else>
      <movie-list-item v-for="movie in filterMovies" :key="movie.id" :movie="movie"></movie-list-item>
    </div>
  </div>
</template>

<script>
// 1-1. 저장되어 있는 MovieListItem 컴포넌트를 불러오고,
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  // 1-2. 아래에 등록 후
  components: {
    MovieListItem,
  },
  data () {
    return {
      // 활용할 데이터를 정의하시오.
      selectedGenreId: 0,
      filterMovies: []
    }
  },
  // 0. props 데이터를 받기 위하여 설정하시오.
  // genres와 movies 모두 타입은 Array이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.

  // 여기서 사용할 데이터를 쓰겠다.(부모로부터 받은)
  // 내가 부모로부터 받아서 여끼서 쓰겠다.
  props: {
    genres: {
      type: Array,
      required: true
    },
    movies: {
      type: Array,
      required: true
    },
  },

  // 2-3.에서 이야기하는 특정한 함수는 selectedGenreId의 값이 변경될 때마다 호출 됩니다.
  // 드랍다운에서 장르를 선택하면, 해당 영화들만 보여주도록 구현 예정입니다.
  // 주의할 것은 직접 부모 컴포넌트의 데이터를 변경할 수 없다는 점입니다.
  // 완료 후 

  watch: {
    selectedGenreId: {
      handler() {
        this.filterMovies = this.movies.filter(movie => {
          return movie.genre_id === this.selectedGenreId
        })
      }
    }
  },
}
</script>

<style>
select {
  display: block;
  width: 50% !important;
  margin: 2rem auto !important;
}
</style>