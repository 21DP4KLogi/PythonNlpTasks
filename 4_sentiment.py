import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from util_translate import *

sia = SentimentIntensityAnalyzer()

def sentiment(text):
    return sia.polarity_scores(text)

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
        ]

for i in sentences:
    print(i)
    translated = lv2en(i)
    print(translated)
    print(sentiment(translated), "\n")

# Source:
# https://medium.com/@umarsmuhammed/how-to-perform-sentiment-analysis-using-python-step-by-step-tutorial-with-code-snippets-4ac3e9747fff
