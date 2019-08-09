## 03.py 가이드 라인
import requests, json, csv
from pprint import pprint
from decouple import config
from datetime import datetime, timedelta
### 1. 감독 이름 가져오기

#1. movie.csv 에서 감독 이름 가져오기 (DictReader) - 리스트

result=[]
with open('movies.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for reads in reader:
        code = reads.get('감독')
        result.append(code)
# print(result)
results={}


for pd_name in result:
    peopleNm = pd_name
    key = config('MV_KEY')
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?peopleNm={peopleNm}&key={key}&itemPerPage=100'

    api_data = requests.get(url).json()
    # pprint(api_data)
    peoples = api_data.get('peopleListResult').get('peopleList')[0]
    code = peoples.get('peopleCd')
    role = peoples.get('repRoleNm')
    if code not in results and role == '감독': 
      results[code] = {
        '감독코드': peoples.get('peopleCd'),
        '감독명': peoples.get('peopleNm'),
        '감독명(영문)': peoples.get('peopleNmEn') if peoples.get('peopleNmEn') else None,
        '필모': peoples.get('filmoNames') 
  
      } 
    # print(results)
with open('director.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['감독코드', '감독명', '감독명(영문)', '필모']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for value in results.values():
      # print(value)
      writer.writerow(value)


