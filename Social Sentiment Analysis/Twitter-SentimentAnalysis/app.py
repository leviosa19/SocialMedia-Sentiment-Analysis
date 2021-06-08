from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'TpY26ZlRYX47IM2rRPuwJh3F9'
consumer_secret = 'tpfMISHQ4RwglkBUw2YXaL2gT4pWJDIwWOjdm9g3UEwYHCOs70'

access_token = '2716777751-YcqFbh8qv8Gf3CIsS4ZeCPvKeswsRol2PA1haWG'
access_token_secret = 'mBdEMGIQMwQcRk43vZzJ40DwKC69PG3br5Nc276KPZ8ar'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
@app.route("/twitter")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


if __name__ == '__main__':
    app.run(debug = True, port = '5002')