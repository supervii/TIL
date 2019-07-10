import requests
from bs4 import BeautifulSoup

url ='https://www.naver.com'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')
realtimes = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
# for i in realtime:
#     print(i.text)

with open('realtimerank_naver.txt', 'w', encoding='utf-8') as f:
    for realtime in realtimes:
        f.writelines(f'{realtime.text}\n')
#    for i in realtime:
#          f.write(f'{i.text}\n')
