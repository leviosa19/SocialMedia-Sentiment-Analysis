from flask import Flask, url_for, render_template, jsonify, request, redirect
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import collections
import re
import os
import json

import matplotlib.pyplot as plt


app = Flask(__name__)

UPLOAD_FOLDER = '/uploaded_files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

analyser = SentimentIntensityAnalyzer()


@app.route('/')
@app.route('/index', methods = ['POST', 'GET'])
@app.route('/facebook', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/get-sentiment/<message>')
def sentiment(message):
	text = TextBlob(clean_text(message))
	
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity }
	snt = analyser.polarity_scores(clean_text(message))
	response.update(snt)
	return jsonify(response)


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':
        f = request.files['file']
        f.save("uploaded_files/" + f.filename)
        return render_template("save.html", name = f.filename)  



def clean_text(text):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())



@app.route('/upload/<string:name>', methods=['POST', 'GET'])
def upload(name):
	pos = []
	neg = []
	neu = []
	minus = 0
	plus = 0
	none = 0
	counts = 0
	sentiment_file = []
	x = []

	with open('uploaded_files/' + name, encoding="utf8") as f:
		for line in f:
			counts += 1
			# print(counts, ":", line)
			text = TextBlob(clean_text(line))
			snt = analyser.polarity_scores(clean_text(line))

			# print(snt)
			snt.pop("compound")
			res = not any(snt.values())
			if res:
				Keymax = 'neu'
			else:
				Keymax = max(snt, key=snt.get)
				
			# bar.append(snt.get(Keymax) * 100)
			# print(Keymax, ": ", snt.get(Keymax) * 100, "%")
			# print()
			# print()

			if Keymax == 'pos':
				pos.append(snt.get(Keymax))
				plus += 1
			elif Keymax == 'neg':
				neg.append(snt.get(Keymax))
				minus += 1
			else:
				neu.append(snt.get(Keymax))
				none += 1
			
			sentiment_file.append([{'line':line, 'count':counts, 'snt':snt, 'max_sentiment':Keymax}])
		
		x.append([{'pos': plus, 'neu': none, 'neg': minus }])

	# per_pos = (sum(pos) / len(pos)) * 100
	# per_neg = (sum(neg) / len(neg)) * 100
	# per_neu = (sum(neu) / len(neu)) * 100

	y = plus + minus + none
	per_pos_1 = (plus * 100) / y
	per_neg_1 = (minus * 100) / y
	per_neu_1 = (none * 100) / y

	# Pie chart
	legend = 'Sentiment Analysis'
	labels = ["Positive", "Neutral", "Negative"]
	values = [per_pos_1, per_neu_1, per_neg_1]
	# colors = ['#57CE2F', '#7DC1C1', '#FF1A1A']

	# Bar plot
	files = open('uploaded_files/' + name, 'r', encoding="utf8")
	files = files.read()
	stopWords = set(line.strip() for line in open('stopwords.txt'))
	stopWords = stopWords.union(set(['a', 'i', 'mr', 'ms', 'mrs', 'one', 'two', 'said']))
	wordCount = collections.defaultdict(int)
	pattern = r"\W"
	for word in files.lower().split():
		word = re.sub(pattern, '', word)
		if word not in stopWords:
			wordCount[word] += 1
	
	mc = sorted(wordCount.items(), key=lambda k_v: k_v[1], reverse=True)[:20]
	words_count = []
	for word, count in mc:
		if word == '':
			del word
		else:
			words_count.append([{ 'word':word, 'counts':count }])
	mc = dict(mc)
	# namesss = list(mc.keys())
	# valuesss = list(mc.values())

	return render_template('save.html', upload = sentiment_file, name = name, x = x, values=values, labels=labels, legend=legend, mc = words_count)


@app.route('/sentiment', methods=['POST', 'GET'])
def goto_sentiment():
	return redirect('http://127.0.0.1:5000/sentiment')


@app.route('/twitter', methods=['POST', 'GET'])
def goto_twitter():
	return redirect('http://127.0.0.1:5002/twitter')


if __name__ == '__main__':
    app.run(debug = True, port = '5001')