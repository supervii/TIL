from flask import Flask
app = Flask(__name__)

@app.route('/ssafy')
def hello():
    return 'This is ssafy!'