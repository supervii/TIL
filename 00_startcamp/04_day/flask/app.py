from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')



@app.route('/ssafy')
def ssafy():
    return 'Thiz iz SSAFY!'


@app.route("/dday")
def dday():
     # 오늘날짜
    today_time = datetime.now()
    # 수료날짜
    endgame = datetime(2019, 11, 29)
    # 수료날짜 - 오늘 날짜
    dday = endgame - today_time

    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return ' <h1>This is html TAG</h1>'


@app.route('/html_line')
def html_line():
    # 다큐먼트 스트링
    return """
    <h1>여러줄을 보내봅시다 </h1>
    <ol>
    <li>이건 줄이있는 라인</li>
    </ol>
    <ul>
    <li>이건 점이있는 라인</li>
    </ul>
    """

# variable routing
@app.route('/greeting/<name>')
# @app.route('/greeting/<string:name>') str값만 생략 가능 int 경우는 표시해줘야함 
# string	(default) accepts any text without a slash
# int	accepts positive integers
# float	accepts positive floating point values
# path	like string but also accepts slashes
# uuid	accepts UUID strings
def greeting(name):
#     return f'반갑습니다! {name}님'
    return render_template('greeting.html',html_name=name)    


@app.route('/cube/<int:number>')
def cube(number):
#     answer = f'{number}의 세제곱은 {number**3} 입니다.'
# #     return f'<h1>{number}의 세제곱은 {answer}입니다</h1>'
#     return render_template('cube.html', cube=answer)
    result = number**3
    return render_template('cube.html', result=result, number=number)

@app.route('/lunch/<int:number>')
def people(number):
    menu_list = ['밥','햄버거','피자','치킨','짜장면','짬뽕']
    # order = random.sample(menu_list,number)
    # # return f'오늘의 점심은 {order}'
    for i in menu_list:
        return f'오늘의 점심은 {random.sample(i,number)}'


# render tamplate
@app.route('/movie')
def movie():
	movies = ['toystory4', 'spiderman', 'aladin', 'lionking', 'parasite']
	return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
	return render_template('ping.html')

@app.route('/pong')
def pong():
	print(request.args)
	name = request.args.get('data')
	return render_template('pong.html',name=name)


# https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
	return render_template('naver.html')

# https://www.google.com/search?
@app.route('/google')
def google():
	return render_template('google.html')


@app.route('/wgmm')
def when_god_make_me():
	return render_template('wgmm.html')

@app.route('/itsu')
def this_is_u():
	name = request.args.get('data')
	cha_list = ['단순함', '똑똑함','능력','재운','외모','매력']
	cha = random.sample(cha_list,3)
	return render_template('/itsu', name=name, cha=cha)