from textblob import TextBlob,Word
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['post'])
def data():
    s_word = request.form.get('word')
    data = TextBlob(s_word)
    # print(data.correct())
    return render_template('home.html',data=data.correct())

app.run(host = '0.0.0.0', port = 8080)   
