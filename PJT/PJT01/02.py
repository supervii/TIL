import requests, json, csv
from pprint import pprint
from decouple import config
from datetime import datetime, timedelta

result=[]
with open('boxoffice.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for reads in reader:
        code = reads.get('movieCd')
        result.append(code)
# print(result)
# print(type(result))
results={}


for code_detail in result:
    movieCd = code_detail
    key = config('MV_KEY')
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'

    api_data = requests.get(url).json()
    # pprint(api_data)
    movies = api_data.get('movieInfoResult').get('movieInfo')
    # print(type(movies))

    codes = movies.get('movieCd')
    results[codes] = {
        '영화 대표코드': movies.get('movieCd'),
        '영화명(국문)': movies.get('movieNm'),
        '영화명(영문)': movies.get('movieNmEn'),
        '영화명(원문)': movies.get('movieNmOg'),
        '관람등급': movies.get('audits')[0].get('watchGradeNm') if movies.get('audits') else None,
        '개봉연도': movies.get('openDt'),
        '상영시간': movies.get('showTm'),
        '장르': movies.get('genres')[0].get('genreNm'),
        '감독': movies.get('directors')[0].get('peopleNm') if movies.get('directors') else None
    }
# print(results)
with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['영화 대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for value in results.values():
        print(value)
        writer.writerow(value)