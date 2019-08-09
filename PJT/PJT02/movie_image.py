import requests, json, csv
from pprint import pprint
from decouple import config



with open('movie_naver.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    result= {}
    for row in reader:
        result.update({row['영진위 영화 대표코드'] : row['영화 썸네일 이미지의 URL']})
    # pprint(result)


for key, url in result.items():
    with open(f'images/{key}.jpg', 'wb') as f:
        response = requests.get(url).content
        f.write(response)
