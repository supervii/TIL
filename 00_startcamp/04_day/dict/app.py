import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# 로또회차/내 번호 입력 페이지
# 결과 페이지 

@app.route('/lotto_check')
def lotto_check():
    return render_template('/lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    # 회차번호를 가져온다 
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # json 형태로 바꿔준다 (크롬에서 보는 결과와 동일한 모습)
    lotto = res.json()

    # 당첨 번호 6개 가져오기
    winner = [] 
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    # 당첨 번호랑 내번호 비교, 내번호 리스트 만들기 
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    #  등수 가리기(몇개 맞았나 교집합 필요 )
    matched = 0
    # 내번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인 
    for num in numbers:
        if num in winner:
            matched += 1 
    if matched == 6:
        result = '1등 입니다!'
    elif matched ==5:
        if lotto['bnusNo'] in numbers:
            result = '2등 입니다!'
        else:
            result = '3등 입니다!'
    elif matched == 4:
        result = '4등 입니다.'
    elif matched ==3:
        result ='5등 입니다.'
    else:
        result = '다음 기회에..'

    return render_template('lotto_result.html', 
                            winner=winner,
                            numbers=numbers,
                            result=result)
    

