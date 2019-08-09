import requests, json, csv
from pprint import pprint
from decouple import config


results = {}
with open('movie.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    result= {}
    for row in reader:
        result.update({row['영화 대표코드'] : row['영화명(국문)']})
    # print(result)
        # code = reads.get('영화 대표코드')
        # code_2 = reads.get('영화명(국문)')
        # mv_cd.append(code)
        # mv_nm.append(code_2)    

    #     result = zip(mv_cd, mv_nm)
    # dic_cdnm = dict(result)
   

url = 'https://openapi.naver.com/v1/search/movie.json'

for movieCd, movieNm in result.items():
    # print(movieNm)
    CLIENT_ID = config('NAVER_CLIENT_ID')
    CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
    HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}
        
    address = f'{url}?query={movieNm}'
    response = requests.get(address, headers=HEADERS).json()
    movies = response.get('items')[0]
    # codes = movies.get('title')
    # print(codes)
    results[movieNm] = {
        '영진위 영화 대표코드' : movieCd,
        '하이퍼텍스트 link' : movies.get('link'),
        '영화 썸네일 이미지의 URL' : movies.get('image'),
        '유저 평점' : movies.get('userRating')

    }

# pprint(results)

with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지의 URL', '유저 평점']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for value in results.values():
        print(value)
        writer.writerow(value)