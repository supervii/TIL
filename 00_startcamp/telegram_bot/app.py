from flask import Flask, render_template, request
import requests, pprint
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


# @app.route('/')
# def hello():
#     return 'Hi there!'

# @app.route('/write')
# def write():
#     return render_template('write.html')


# @app.route('/send')
# def send():
#     text = request.args.get('message')

#     requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

#     return render_template('send.html')


@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 데이터 구조 print 해보기
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None:
        # 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # 한글키워드 받기
        # '/번역 '으로 입력이 시작 된다면, 파파고로 번역이 동작한다. 
        if  text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
               }
            data = {'source': 'ko', 'target':'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        if  text[0:4] == '/한중 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
               }
            data = {'source': 'ko', 'target':'zh-CN', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        if  text[0:4] == '/한태 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
               }
            data = {'source': 'ko', 'target':'th', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')



        if text[0:4] == '/로또 ':
            num  = text[4:]
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            lotto = res.json()

            winner = [] 
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'로또 {num} 회차의 당첨 번호는 {winner} 입니다. 보너스 점수는 {bonus_num}.'

        if text[0:5] == '/실시간 ':
            url = 'https://www.naver.com/'
            html = requests.get(url).text
            soup = BeautifulSoup(html,'html.parser')
            realtime = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
            for i in realtime:
                text = i.text
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200
