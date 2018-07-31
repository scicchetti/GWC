'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweeter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
tweets = []

polarity_values = []

for tweet in tweetData:
    tweets.append(tweet["text"])
    tweets.append(" ")
giant_string = " ".join(tweets)

list_of_words = giant_string.split()

positive = []
negative = []
neutral = []

for word in list_of_words:
    word = word.lower().rstrip().lstrip()
if "http" in word:
    continue
if word 
for word in list_of_words:
    word_polarity = TextBlob(word).polarity_values
    if word_polarity <  -0.25:
        negative.append(word)
    elif word_polarity < 0.25:
        neutral.append(word)
    else
    positive.append(word)

word_count = {}
for word in list_of_words:
    word = word.lower().lstrip()
    if "http" in word:
        continue
    if word[0] == "#" or word[0] == "@":
        word = word[1:]
    if len(word) < 4:
        continue
    if word[-1] in {",", ".", "?", ":", "!", "/"}:
        word = word[:-1]
    word_count[word] = word_count.get(word, 0) + 1

word_count2 = {}
for word, count in word_count.items():
    if count < 2:
        continue
    else:
        word_count2[word] = count

print(word_count2)

wordcloud = WordCloud().generate_from_frequencies(word_count2)
plt.imshow(wordcloud, interpolation="bilinear")
plt.show()

# word_count[word] = word_count.get(word, 0) + 1
# print(len(word_count))

tb = TextBlob(giant_string)
# Continue your program below!

# Textblob sample:
# Continue your program below!

# Textblob sample:
# while True:
#     phrase = input("Enter a phrase: ")
#     tb = TextBlob("")
#     print(tb.polarity)
