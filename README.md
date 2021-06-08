# Social Media Sentiment Analysis ( Facebook, Twitter )

In this project their are three modules are included which named ***SentimentAnalysis, FB-SentimentAnalysis, Twitter-SentimentAnalysis***. 
Each module is consist of particular sentiment analysis app. This is web-based app run with Flask framework. 

I personally suggest to use **Visual Studio** IDE.

**NOTE: You need internet connectivity to run all this three modules.**

To run this app, follow below steps instructions.

1. Open all three module in respective IDE simultaneously.
2. Install **Flask** using following command. ( You need Python3 or latest version in your system. )
For more info referred Flask installation [Documentation](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask/)
```bash
$ pip install Flask
```
Flask is now installed.
 
3. Install **NLTK**. For more info, referred [NLTK Documentation](https://www.nltk.org/install.html)
```bash
$ pip install nltk
```

4. Install **TextBlob**. For more info, referred [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/install.html).
```bash
$ pip install -U textblob
```

5. Install **Tweepy**. For more info, referred [Tweepy Documentation](http://docs.tweepy.org/en/latest/install.html).
```bash
$ pip install tweepy
```

6. Run all three **app.py** file simultaneously which is present in all three modules and run this file simaltanously in respective IDE using following command.
```bash
$ python app.py
```
7. After running all three **app.py** file, click on respective link given in the terminal or click this [link](http://127.0.0.1:5000/sentiment).

## Facebook Sentiment Analysis 
After successfully running of **app.py** file, click on the URL displayed in the termonal or [Click Here](http://127.0.0.1:5001/facebook).

In this module, sentiment of facebook data/comments is done. for this, you need to upload .txt file of facebook data/comments 
which is present in **FB-SentimentAnalysis/fb_files/**. Upload any .txt file to get sentiment information.

## Twitter Sentiment Analysis 
In this module, live sentiment of twitter data is to be done.

To run this module, you need to write consumer key & secret number and access token & secret of your twitter app to 
get live sentiment analysis. Write this keys in **app.py** file.

To get this keys open [Twitter App](https://developer.twitter.com/en/apps)
```bash

consumer_key = 'consumer_key' # Write consumer key here
consumer_secret = 'consumer_secret' # Write consumer_secret key here

access_token = 'access_token' # Write access_token key here
access_token_secret = 'access_token_secret' # Write access_token_secret key here

```

Click on respective URL displayed in the terminal after run or [Click Here](http://127.0.0.1:5002/twitter)

In the web view, write any twitter handler name to get the sentiment, in the text field and test the operation. 
