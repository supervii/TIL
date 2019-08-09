## **파이썬을 활용한 데이터 수집2** **I** 프로젝트

### 1. 프로젝트 소개:blue_book:

 본 프로젝트는 데이터 수집1을 응용한 데이터 수집 프로젝트입니다.  프로젝트는 크게 두 파트로 나뉘어집니다.

첫째, 영화진흥위원회보다 조금 더 복잡한 요청과정을 통해서 영화의 정보를 가져와서 csv 파일로 생성 후 

둘째, 생성된 csv 파일에서 이미지의 url 주소를 가져와 새로운 image 폴더안에 영화 코드의 이름으로 

해당 영화의 이미지를 저장시키는 과정입니다.  개발은 python 3.7.3 버전에서 진행하였고 vs code에서 작성하였습니다. 필수 라이브러리로는 requests, json, decouple등을 활용하였습니다.



### 2.각각 .py에 대한 설명

#### :notes: movie_naver.py

- 기존의 movie.csv에서 영화 대표코드와 영화명(국문)을 딕셔너리 형태로 가져옵니다. 

  - .update의 활용법을 정확히 이해하지 못한 시행착오 

    ```python
    with open('movie.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result= {}
        for row in reader:
    		 code = row.get('영화 대표코드')
             code_2 = row.get('영화명(국문)')
             mv_cd.append(code)
             mv_nm.append(code_2)    
    
            result = zip(mv_cd, mv_nm)
         dic_cdnm = dict(result)
       
    ```

  - .update를 사용한 코드

    ```python
    with open('movie.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result= {}
        for row in reader:
            result.update({row['영화 대표코드'] : row['영화명(국문)']})	
    ```

- 가져온 딕셔너리에서 key: 대표코드, val: 영화명을 통해 요청url에 f스트링으로 데이터 요청 및 가져오기

  ```python
  url = 'https://openapi.naver.com/v1/search/movie.json'
  
  for movieCd, movieNm in result.items():
      # print(movieNm)
      CLIENT_ID = config('NAVER_CLIENT_ID')
      CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
      HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}
          
      address = f'{url}?query={movieNm}'
      response = requests.get(address, headers=HEADERS).json()
      movies = response.get('items')[0] #여러개의 유사데이터를 가져오는데 첫번째 데이터가 답
      # codes = movies.get('title')
      # print(codes)
      results[movieNm] = {
          '영진위 영화 대표코드' : movieCd,
          '하이퍼텍스트 link' : movies.get('link'),
          '영화 썸네일 이미지의 URL' : movies.get('image'),
          '유저 평점' : movies.get('userRating')
  
      }
  ```

- 가져온 딕셔너리 형식을 csv 파일에 데이터 입력 후 저장 

- 결과물

  ![무비 네이버 결과물](https://user-images.githubusercontent.com/52685245/61926352-3382f680-afab-11e9-8ff4-4a1f47c2438a.PNG)



#### :notes: movie_img.py

- 위에서 새로 만든 movie_naver.csv에서  내용을 가져옵니다. 첫번째 과정과 유사하여 금방 해결할 수 있었습니다.

  ```python
  with open('movie_naver.csv', newline='', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      result= {}
      for row in reader:
          result.update({row['영진위 영화 대표코드'] : row['영화 썸네일 이미지의 URL']})
      # pprint(result)
  ```

- 가져온 딕셔너리 데이터에서 value값 url로부터 데이터를 가져와 key 값으로 이미지 파일 이름으로 지정하여 미리 만들어둔 images 폴더에 이미지를 저장할 수 있습니다. wb 옵션을 사용하였습니다. 

  ```python
  for key, url in result.items():
      with open(f'images/{key}.jpg', 'wb') as f:
          response = requests.get(url).content
          f.write(response)
  ```

- 결과물

  ![무비 이미지 결과물](https://user-images.githubusercontent.com/52685245/61926623-4e099f80-afac-11e9-8744-35ceb667dcdf.PNG)



### 3. 프로젝트를 통해 느낀점

 첫번째 과정에서 데이터를 가져오는데 시행착오와 데이터 처리에서 문제가 있었지만, 저번 프로젝트에서 배운 방법을 활용하여 잘 해결할 수 있었습니다. 부족한 부분을 서로 물어가봐가면서 보충하여 성공적으로 프로젝트를 마무리 지을 수 있었습니다. 