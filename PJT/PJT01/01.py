import requests, json, csv
from pprint import pprint
from decouple import config
from datetime import datetime, timedelta


result = {}
api_url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
key = config('MV_KEY') 
cal_datetime = datetime(2019, 7, 13)
for week in range(50):
    new_datetime = cal_datetime - timedelta(weeks=week)
    targetDt = new_datetime.strftime('%Y%m%d')
    # print(week)

    realtimerank_mv = f'{api_url}key={key}&targetDt='+targetDt
    api_data = requests.get(realtimerank_mv).json()
    # pprint(api_data)

    movies = api_data.get('boxOfficeResult').get('dailyBoxOfficeList')
    #대표코드 / 영화명 / 누적관계수
    #영화정보가 담긴 딕셔너리 에서 영화대표코드를 추출
    for movie in movies:
        code = movie.get('movieCd') 
        if code not in result: #날짜를 거꾸로 돌아가면서 데이터를 얻기 때문에 
            result[code] ={
                'movieCd': movie.get('movieCd'),
                'movieNm': movie.get('movieNm'),
                'audiAcc': movie.get('audiAcc')
            }
    # pprint(result)



with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'audiAcc')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    
    
    for value in result.values():
        writer.writerow(value)