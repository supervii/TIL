# PJT09 - Vue component

## 1. 프로젝트 개요

> Node 개발 환경과 webpack 및 컴포넌트 기반 구조를 활용하며 axios를 통해 데이터를 비동기적으로 처리하고, Vue.js 를 활용하여 영화 목록 페이지를 구현하는 프로젝트이다.

## 2. 코딩 과정

### `App.vue`

- URL을 통하여 JSON 데이터를 받아와 저장한다.

```javascript
mounted() {
    // 0. mounted 되었을 때, 
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오. 
    const URL_movies = 'https://gist.githubusercontent.com/edujunho-hphk/1a75dbae2f69a33d1519a8703d5afa5c/raw/05bc2a01ad9ad0338bf67a15be321a1e1858ab4f/movies.json'
    axios.get(URL_movies)
      .then(response => {
        this.movies = response.data  
      })
      .catch(error => error)
    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    const URL_genres = 'https://gist.githubusercontent.com/edujunho-hphk/b7d063a9efd11acba51f6dcedcc8c520/raw/d2cae437669b41c7316c426f5451ef34792b9f39/genre.json'
    axios.get(URL_genres)
      .then(response => {
        this.genres = [ 
          {id: 0, name: '전체보기'},
          ...response.data
        ]
      })
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
  },
```

- `axios` 요청을 통하여 `movies.json`데이터를 비동기적으로 받아올 수 있다.
- 장르별 보기에서 `전체보기` 탭을 만들기 위해 `id: 0` 인덱스에 전체보기를 추가하였다.
- 가져온 데이터를 아래와 같이 `MovieList.vue` 컴포넌트로 보내준다.

```HTML
<movie-list :genres="genres" :movies="movies"></movie-list>
```

------

### `MovieList.vue`

- 먼저 코드 구성에 필요한 `MovieListItem.vue`를 `import` 한다.

```javascript
// 1-1. 저장되어 있는 MovieListItem 컴포넌트를 불러오고,
import MovieListItem from './MovieListItem.vue'
```

- `v-for`장르 선택 폼을 만들어 준다.

```html
<select v-model="selectedGenreId" class="form-control">
      <option v-for="genre in genres" v-bind:key="genre.id" :value="genre.id">{{ genre.name }}</option>
</select>
```

- 장르를 변경할때마다 변화를 감지하기 위하여 `watch`속성을 이용하고, `genre id`값에 따른 영화들을 `filter`로 분류하여 저장한다.

```javascript
watch: {
    selectedGenreId: {
      handler() {
        this.filterMovies = this.movies.filter(movie => {
          return movie.genre_id === this.selectedGenreId
        })
      }
    }
  }
```

- `selectedGenreId`에 담기 `genre id`값에 따라 조건문으로 분기하여 일치하는 장르의 영화들만 보여준다.

```html
<div class="row mt-5" v-if="selectedGenreId === 0">
      <movie-list-item v-for="movie in movies" :key="movie.id" :movie="movie"></movie-list-item>
    </div>
    <div class="row mt-5" v-else>
      <movie-list-item v-for="movie in filterMovies" :key="movie.id" :movie="movie"></movie-list-item>
    </div>
```

------

`MovieListItem.vue`

```vue
<div class="col-3 my-3">
    <!-- img 태그에 src와 alt값(영화제목)을 설정하시오 -->
    <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.name">
    <!-- 영화 제목을 출력하시오. -->
    <h3>{{ movie.name }}</h3>
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 합니다. -->
    <button class="btn btn-primary" data-toggle="modal" :data-target="'#movie-'+movie.id">영화 정보 상세보기</button>
    <!-- 1-3. 호출하시오.
      필요한 경우 props를 데이터를 보내줍니다.
    -->
    <movie-list-item-modal :movie="movie"></movie-list-item-modal>
  </div>
```

- image 태그의 `:src`에 포스터 url을 넘겨준다.
- `modal`에 연결하기 위해서는 `data-target`속성으로 `data-target="'#movie-'+movie.id"`와 같이 연결점을 지정해 줘야한다.

- modal을 구성하기 위해 `MovieListItemModal`컴포넌트로 `movie`를 다시 보내준다.

-----

`MovielListItemModal.vue`

- Modal의 연결점이 되는 `id` 값을 지정해준다.

```HTML
<div class="modal fade" tabindex="-1" role="dialog" :id="'movie-'+movie.id">
```

- 앞선 컴포넌트에서 변수 `movie`를 전달 받았으니, `movie` 내의 data를 불러올 수 있다.

```html
<!-- 영화 제목을 출력하세요. -->
<h5 class="modal-title">{{ movie.name }}</h5>
<!-- 영화 설명을 출력하세요. -->
<p>{{ movie.description }}</p>
```

------

`장르 선택`

![image](https://user-images.githubusercontent.com/52685322/68453380-bbc69800-0238-11ea-9307-0de8cad09808.png)



`Modal 실행`

![image](https://user-images.githubusercontent.com/52685322/68453412-ced96800-0238-11ea-96c3-311b90c63ba5.png)

## 3. 어려웠던 점

1. `mounted` : 데이터를 생성할 떄 `axios`를 통해서 해결

2. `props` : 부모와 자식간의 데이터를 주고 받는 방식에 있어서, 구조에 대한 이해가 부족하였다.

   - 케밥 스타일로 `ex)<todo-list :dataChil="dataParent"></todo-list>`

3. `장르 전체보기`: JSON 데이터에 없는 전체보기 카테고리를 추가하기 위한 방법을 배웠다.

   `this.genres = [ {id: 0, name: '전체보기'},...response.data ]`

4. `modal 연결하기`: modal을 연결하기 위한 속성으로 `data-target`을 다시 한번 공부하였다.

   `:data-target="'#movie-'+movie.id"`

## 4. 프로젝트를 통해 느낀 점

- 이번 프로젝트를 통하여 Vue-CLI과 컴포넌트의 구조와 상속 관계를 이해하게되었다. 또한, axios를 통해 데이터를 비동기적으로 처리하는 실습을 통해 데이터 송수신 방식을 배울 수 있었다.