#.update()
a = {}

#1
a.update(key='value')
a.update(key:value)

#환경변수 setting decouple

NAVER_CLIENT_ID='m5ajDD5wvso86YKT26cW'
NAVER_CLIENT_SECRET='yd31gvIUW4'


#.py
import requests
from decouple import config

CLIENT_ID = config(NAVER_CLIENT_ID)
CLIENT_SECRET = config(NAVER_CLIENT_SECRET)
HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}


#요청 보내기
url = https://openapi.naver.com/v1/search/blog.json
address = f'{url}?query={movieNm}'
response = requests.get(address, headers=HEADERS).json()

#이미지 파일 저장하기
# 3-1 movie_naver.csv 여기서 영화 코드랑 썸네일 url

# 요청 보내서 응답 작성 하기 

with open(f'images/test.jpg, 'wb') as f:
    response = requests.get(url).content
    f.write(image)


[{'actor': '송강호|조정석|배두나|',
  'director': '우민호|',
  'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1572/157297_P23_134212.jpg',
  'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297',
  'pubDate': '2017',
  'subtitle': 'THE DRUG KING',
  'title': '<b>마약왕</b>',
  'userRating': '6.33'},
 {'actor': '조쉬 허처슨|베니시오 델 토로|',
  'director': '안드레아 디 스테파노|',
  'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1273/127362_P12_101652.jpg',
  'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=127362',
  'pubDate': '2014',
  'subtitle': 'Paradise Lost',
  'title': '파라다이스 로스트: <b>마약</b> 카르텔의 <b>왕</b>',
  'userRating': '8.11'},
 {'actor': '윌 페렐|디에고 루나|가엘 가르시아 베르날|',
  'director': '맷 피드몬트|',
  'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/0892/89265_P11_095001.jpg',
  'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=89265',
  'pubDate': '2012',
  'subtitle': 'House of My Father',
  'title': '알바레즈 형제: <b>마약왕</b>을 제거하라',
  'userRating': '6.50'}]