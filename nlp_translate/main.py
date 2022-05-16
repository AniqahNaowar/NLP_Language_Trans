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
    data.translate(from_lang='en', to='bn')
    # print(data.translate(from_lang='en', to='bn'))
    return render_template('home.html',data=data.translate(from_lang='en', to='bn'))

app.run(host = '0.0.0.0', port = 8080)   
