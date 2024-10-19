import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize, download, sent_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
import csv



nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')


si = SentimentIntensityAnalyzer()

fields = ['PNT_ATRISKNOTES_TX']
dataset1=np.array(pd.read_csv("CORE_HackOhio_subset_cleaned_downsampled 1.csv", skipinitialspace=True, usecols=fields))
#print(dataset1)

sentiments = list()

for i in range(len(dataset1)):
    cleaned_text = ''.join(char for char in str(dataset1[i]) if ord(char) < 128)
    sentiments.append(si.polarity_scores(cleaned_text)['compound'])

with open('vadersentiments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for score in sentiments:
        writer.writerow([score])

print(len(sentiments))

#wordset=set()
#change to range(len(dataset1)):
for i in range(10):
    words=word_tokenize(dataset1.iloc[i,0])
    if '?' in words:
        words.remove('?')
    elif '!' in words:
        words.remove('!')
    elif '...' in words:
        words.remove(('...'))
    elif ',' in words:
        words.remove(('.'))
    elif '.' in words:
        words.remove(('.'))
    for word in words:
        wordset.add(word)


danger=["arc flash", "fire", ""]


wordlist = list(wordset)
print(wordlist)

