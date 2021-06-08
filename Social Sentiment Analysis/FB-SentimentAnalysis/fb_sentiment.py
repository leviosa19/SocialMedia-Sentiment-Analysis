from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import collections
import matplotlib.pyplot as plt

pos = []
neg = []
neu = []
minus = 0
plus = 0
none = 0
counts = 0
bar = []


analyser = SentimentIntensityAnalyzer()

# with open('fb_data.txt') as f:
#    for line in f:
#         obj = TextBlob(line)
#         sentiment = obj.sentiment.polarity
#         if sentiment == 0:
#             print(line, "Neutral: ", sentiment*100, "%")
#             print()
#             neu.append(sentiment)
#             none += 1
#         elif sentiment > 0:
#            print(line, "Positive: ", sentiment*100, "%")
#            print()
#            pos.append(sentiment)
#            plus += 1
#         else:
#            print(line, "Negative: ", sentiment * 100, "%")
#            print()
#            neg.append(sentiment)
#            minus += 1



def clean_text(text):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())



with open('fb_files/fb_eminem.txt', encoding="utf8") as f:
    for line in f:
        counts += 1
        print(counts, ":", line)
        text = TextBlob(clean_text(line))
        snt = analyser.polarity_scores(clean_text(line))

        print(snt)
        snt.pop("compound")
        res = not any(snt.values())
        if res:
            Keymax = 'neu'
        else:
            Keymax = max(snt, key=snt.get)
        
        print(Keymax, ": ", snt.get(Keymax) * 100, "%")
        print()
        print()

        if Keymax == 'pos':
            pos.append(snt.get(Keymax))
            plus += 1
        elif Keymax == 'neg':
            neg.append(snt.get(Keymax))
            minus += 1
        else:
            neu.append(snt.get(Keymax))
            none += 1




# text = TextBlob(clean_text("She is nice"))
# snt = analyser.polarity_scores(clean_text("She is nice"))

# print(snt.values())


per_pos = (sum(pos) / len(pos)) * 100
per_neg = (sum(neg) / len(neg)) * 100
per_neu = (sum(neu) / len(neu)) * 100

x = plus + minus + none
per_pos_1 = (plus * 100) / x
per_neg_1 = (minus * 100) / x
per_neu_1 = (none * 100) / x

print("Total Comments are", plus, "Positive", per_pos, "% ")
print("Total Comments are", minus, "Negative", per_neg, "%")
print("Total Comments are", none, "Neutral", per_neu, "%")

print(sum(pos))
print(x)
print(per_pos_1)
print(per_neg_1)
print(per_neu_1)

# Piechart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [per_pos_1, per_neg_1, per_neu_1]
colors = ['#57CE2F', '#FF1A1A', '#7DC1C1']
plt.pie(sizes, colors=colors, shadow=True, labels = labels, autopct='%0.2f%%')
plt.legend(labels, loc = 'lower left')
plt.axis('equal')
plt.show()


# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
# import numpy as npy
# from PIL import Image


# dataset = open("fb_files/fb_data.txt", "r", encoding="utf8").read()

# def create_word_cloud(string):
#     maskArray = npy.array(Image.open("fb_logo_1.jpg"))
#     cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
#     cloud.generate(string)
#     cloud.to_file("wordCloud.png")
    
#     plt.figure(figsize = (10, 20))
#     plt.imshow(cloud, interpolation='bilinear')
#     plt.axis("off")
#     plt.tight_layout(pad=0)
#     plt.show()
    

# dataset = dataset.lower()
# create_word_cloud(dataset)
