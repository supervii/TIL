# 프레임워크 기반 웹 페이지 구현 |프로젝트

### 1. 프로젝트 소개 &#128195;

 본 프로젝트는 Django, ORM, Form을 활용한 웹페이지를 구현하는 과정을 나타냅니다. Python Web Framework를 통한 데이터 조작과  Object Relational Mapping에 대한 이해, Template Variable을 활용한 Template 제작, Static 파일 관리의 기본 지식이 필요합니다.



### 2. 과정 및 파일에 대한 설명

###### 1. Index 페이지

>###### index.html에 요청 URL /movies/ 으로 설정하고 데이터 베이스에 존재하는 모든 영화의 목록을 포시하며 , title과 score를 표시합니다. 
>
>###### title 을 클릭 시, 해당 영화 정보 조회 페이지로 이동합니다. 영화목록최상단에 새 영화 등록 링크가있으며,클릭시 영화 정보 생성 Form 페이지로 이동합니다.
>
>###### 목록 상단에 영화와 관련한 이미지를 삽입합니다. 해당 이미지는 반드시 서버에 저장된 이미지를 사용합니다.

가장 기본적인 과정으로 모델 폼에서 정보를 가져와서 보여줍니다.

###### 2. 영화정보 생성

>###### 요청 URL은 GET /movies/create/ 입니다. URL은 적절한 name을 가집니다. 
>
>###### Form에 작성된 정보는 Form Submit 버튼 클릭 시 영화 정보 생성 페이지로 생성 요청 (request)과 함께 전송됩니다. 
>
>###### 요청 URL은 POST /movies/create/ 입니다. URL은 적절한 name을 가집니다. 이전 페이지로부터 전송 받은 데이터를 검증한 후 데이터베이스에 저장합니다. 
>
>###### 검증에 실패한 경우 영화 정보 생성 Form 으로 Redirect 합니다. 
>
>###### 해당 페이지에서 저장한 영화 정보를 조회하는 영화 정보 조회 페이지로 Redirect 합니다. 

forms.py에서  설정한 내용을 바탕으로 이전에 일일이 가져오던 정보를 한번에 가져올 수 있습니다. 

###### 3. 영화정보조회

>###### 요청 URL은 /movies/1/ , /movies/2/ 등 이며, 동적으로 할당되는 부분이 존재합니 다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다. URL은 적절한 name을 가집니다. 
>
>###### 해당 Primary Key를 가진 영화의 **모든 정보**가 표시됩니다. 
>
>###### 영화정보의 최하단에는 목록, 수정, 삭제 링크가있으며,클릭시각각 영화 목록,해당 영 화 정보 수정 Form, 해당 영화 정보 삭제 페이지로 이동합니다. 

detail.html에 관한 내용을 만들고 시각화 하는 과정입니다.

###### 4. 영화정보 수정

> ###### 요청 URL은 GET /movies/1/update/ , /movies/2/update/ 등 이며, 동적으로 할 당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다. URL은 적절한 name을 가집니다. 
>
> ###### 해당PrimaryKey를 가진 영화정보를 수정할 수 있는Form이 표시되며, 영화 정보 생성 Form 과 동일한 input을 가지고 있습니다. 
>
> ###### Form에 작성된 정보는 Form Submit 버튼 클릭 시 영화 정보 수정 페이지로 수정 요청 (request)과 함께 전송됩니다. 
>
> ###### 요청 URL은 POST /movies/1/update/ , /movies/2/update/ 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다. URL은 적절한 name을 가집니다. 
>
> ###### 해당 Primary Key를 가진 영화 정보를 이전 페이지로부터 전송 받은 데이터로 변경하여 데이터베이스에 저장합니다. 
>
> ###### 해당 페이지에서 수정한 영화 정보를 조회하는 영화 정보 조회 페이지로 Redirect 합니다. 

CRUD에서 update에 해당하는 내용으로 전송받은 데이터를 데이터베이스에 저장하여 수정합니다.

###### 5. 영화 정보 삭제

>###### 요청 URL은 /movies/1/delete/ , /movies/2/delete/ 등 이며, 동적으로 할당되 는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다. URL은 적절한 name을 가집니다. 
>
>###### 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다. 
>
>###### 영화 정보 목록 페이지로 Redirect 합니다. 

삭제과정도 POST 방식으로 처리하는데 어려움을 가지고 시간을 소비하였습니다.

###### 6. 영화 한줄평 생성

> ###### 한줄평 작성을 위한 Form은 영화 정보 조회 페이지에서 제공됩니다. 
>
> ###### 요청 URL은 POST movies/1/reviews/ , movies/2/reviews/ 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다. URL은 적절한 name을 가집니다. 
>
> ###### 영화 정보 조회 페이지로 Redirect 합니다. 

detail 페이지에서 간단한 리뷰를 남길 수 있는 (comment) 시스템을 만들어 줍니다. 간단한 평과 평점을 남길 수 있습니다.

#### 결과물

<img width="431" alt="Screen Shot 2019-10-18 at 4 58 44 PM" src="https://user-images.githubusercontent.com/52685245/67076802-dc1aae00-f1c8-11e9-9ac5-1df848cd36a6.png">

Index 페이지

<img width="434" alt="Screen Shot 2019-10-18 at 4 59 03 PM" src="https://user-images.githubusercontent.com/52685245/67076826-ed63ba80-f1c8-11e9-85ef-c72719dc0a75.png">

Create(form)페이지

<img width="384" alt="Screen Shot 2019-10-18 at 4 59 25 PM" src="https://user-images.githubusercontent.com/52685245/67076848-f81e4f80-f1c8-11e9-8c3a-d8c4859d80c5.png">

Detail 페이지

<img width="431" alt="Screen Shot 2019-10-18 at 4 59 42 PM" src="https://user-images.githubusercontent.com/52685245/67076877-066c6b80-f1c9-11e9-929d-f1c7d3f38884.png">

Update(form)페이지



### 3. 프로젝트를 통해 느낀점

상대적으로 앞부분보다 짧은 학습기간과 여러 수업의 혼용으로 Django form에 대해 어려운 점이 있었지만 문제를 해결해가면서 다시 한번 학습할 수 있는 기회를 가졌습니다. CRUD 실습을 통해 Django, ORM, Form의 활용법을 다시 한번 익힐 수 있었습니다. 