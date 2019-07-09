import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(html, 'html.parser')
usexchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
jpexchange = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value').text
cnexchange = soup.select_one('#exchangeList > li > a.head.cny > div > span.value').text
print('미국환율=',usexchange,'일본환율=',jpexchange,'중국환율=',cnexchange)
