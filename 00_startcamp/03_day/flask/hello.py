from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'say BYE to your life ^^'

@app.route('/ssafy')
def ssafy2():
    return 'This is ssafy!'