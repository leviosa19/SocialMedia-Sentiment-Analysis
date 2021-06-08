from flask import Flask, render_template, jsonify
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import re

analyser = SentimentIntensityAnalyzer()

app = Flask(__name__)


@app.route('/')
@app.route('/sentiment')
def index():
    return render_template("index.html")


@app.route('/get-sentiment/<message>')
def sentiment(message):
	text = TextBlob(clean_text(message))
	
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity }
	snt = analyser.polarity_scores(clean_text(message))
	response.update(snt)
	return jsonify(response)


@app.route('/vader/<message>')
def vaderSent(message):
	snt = analyser.polarity_scores(clean_text(message))
	return jsonify(snt)


def clean_text(text):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


if __name__ == "__main__":
    app.run(debug=True)
