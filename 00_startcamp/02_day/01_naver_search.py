import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')
realtime = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
for i in realtime:
    print(i.text)

# 두번째 커밋을 위한 주석 !!
# 홈테스트를 위한 주석 !!