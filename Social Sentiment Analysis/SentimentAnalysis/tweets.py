from flask import Flask, jsonify, render_template
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index1.html")

class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'zxFl9XJMEDB0p7S5BOzzat0ff'
        consumer_secret = '6ZY7Lz8zpJJ2fNkOJev8X4KxeB3SMUuVG9xrHkV0JVCsQ6bhkX'
        access_token = '2716777751-cjybKzjA4AgoIGJD4Iqn0T0uf7QGPyHgsE8TpMu'
        access_token_secret = 'Srd41LGppPIHUVqBH0EO6O4dgmpsc4vUXHWb5fuGPMbsc'
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets 
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e))

@app.route("/get-sentiment/<username>")
def sentiment(username):
   # creating object of TwitterClient Class 
   api = TwitterClient() 
   # calling function to get tweets 
   tweets = api.get_tweets(query = username, count = 1000) 
  
   # Positive tweets from tweets 
   ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
   # Negative tweets from tweets 
   ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    
   # percentage of positive tweets 
   # try:
   #    a = "Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets))
   #    render_template("index1.html", data = {a})
   # except ZeroDivisionError:
   #    a = "Positive tweets percentage: 0%"
   #    render_template("index1.html", data = {a})

   if tweets['sentiment'] == 'positive':
      a = 100 * len(ptweets) / len(tweets)
      render_template("index1.html", data={a})
   elif tweets['sentiment'] == 'negative':
      b = 100 * len(ntweets) / len(tweets)
      render_template("index1.html", data={b})
   else:
      c = "Fuck OFF then"
      render_template("indexx1.html", data = {c})


if __name__ == "__main__":
    app.run(debug=True)
