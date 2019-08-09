## HTML/CSS 를 활용한 웹 사이트 구성 | 프로젝트

### 1. 프로젝트 소개 &#128195;

​	본 프로젝트는 HTML과 CSS를 활용하여 index.html의 마크업과 layout.css를 작성하는 프로젝트 입니다. 필수 요소들을 다운 받아서 필요한 파일들을 준비 후, 정해진 명세서에 맞추어 작성을 하였습니다. 학습을 통해 배운시멘틱 태그를 활용하여 전체적인 html의 틀을 잡고 자료를 토대로 class 마크업과 layout.css 에 선택자를 활용하여 속성을 주었습니다. 이를 통해 영화 추천 사이트의 메인 레이아웃을 구성할 수 있었습니다.



### 2. 각각의 파일에 대한 설명

#### &#127915; index.html

- 먼저 ! 를 통해 html의 기본적인 틀을 잡아줍니다.  그 후 명세서에 따라 기초 사항을 변경해줍니다.

  > DOCTYPE은 html
  >
  > html의 언어는 한국어(ko)
  >
  > meta 태그에 인코딩 설정을 UTF-8로 설정 
  >
  > meta 태그에 기본 viewport 설정. (width: device-width, initial-scale: 1.0) title 태그는 영화추천사이트 라고 설정

- body 부분에 header와 nav, section, div, footer로 크게 섹션을 만들어 주고 필요한 데이터들을 채워 줍니다.

  ```html
    <header>
    </header>
    <section id="section-title">
    </section>
    <div id="content">
    </div>
    <footer>
      Project #3 created by ___ , 2019
    </footer>
  ```

  

- 필요한 부분들을 채워 줍니다.  클래스와 아이디를 할당하여 css파일과 작동 할수 있도록 link 하여줍니다.

- 각각의 목록을 구성하여 태그에 맞게 정리하여 줍니다.

#### &#127915; layout.css

- header를 상단에 고정시키며(sticky) 다른 영역보다 우선하여 볼 수 있도록 작성.

  ```html
  z-index: 999;
  position: fixed;
  top: 0;
  ```

  배우지 않았던 z-index를 구글 검색을 통해 해결 하였습니다.

- nav 부분 항목을 오른쪽 정렬과 한줄로 만들고 여백 지정 및  bullet point 제거

  ```html
  float: left;
  margin-left: 10px;
  margin-right: 10px;
  list-style-type: none;
  ```

- nav-items의 링크 기본색을 변경

  ```html
  color: darkcyan;
  ```

- nav-items의 마우스 오버시 적용 사항들

  ```html
  color: yellow;
  text-decoration: none;
  ```

- section 부분 처리

  ```html
  background-image: url(images/background.jpg);
  background-size: cover;
  background-position: center;
  text-align: center;
  line-height: 300px;
  
  font-size: 3rem;
  ```

- aside의 영역 위치 

  ```html
  position: absolute;
  top: 0;
  
  padding:0;
  
  list-style-type: none;
  ```

  영역 위치에 관해 모르는 부분이라 많이 헤매었습니다.

  

- footer

  ```html
  position: fixed;
  bottom: 0;
  text-align: center;
  line-height: 50px;
  ```



### 3. 프로젝트를 통해 느낀점

html은 시멘틱 태그와 필요한 class와 id  할당을 통해 css에서 하나하나 조작을 해주어야합니다. 

이를 위해 깔끔한 구성과 흐름으로 작성하여야 한다는 점을 배웠고, 더 많은 연습을 통해 익숙해져야 할 필요성을 느꼈습니다. 