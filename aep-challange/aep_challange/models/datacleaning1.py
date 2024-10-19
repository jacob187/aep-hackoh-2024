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


fields = ['QUALIFIER_TXT','PNT_ATRISKNOTES_TX','PNT_ATRISKFOLWUPNTS_TX']
df=(pd.read_csv("CORE_HackOhio_subset_cleaned_downsampled 1.csv", skipinitialspace=True, usecols=fields))
df['combined']= df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
dataset1 = np.array(df['combined'])
print(dataset1)


sentiments = list()

for i in range(len(dataset1)):
    cleaned_text = ''.join(char for char in str(dataset1[i]) if ord(char) < 128)
    sentiments.append(si.polarity_scores(cleaned_text)['compound'])

np.save('vadersentiments.npy',np.array(sentiments))

'''
with open('vadersentiments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for score in sentiments:
        writer.writerow([score])
'''

print(len(sentiments))

wordset=set()
#change to range(len(dataset1)):

sample =20000

def clean(text):
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\[NAME\]', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = [stemmer.stem(word) for word in text]
    text = " ".join(text)
    return text


for i in range(sample):
    words=word_tokenize(dataset1[i])
    if '...' in words:
        words.remove(('...'))
    elif '[NAME]' in words:
        words.remove(('[NAME]'))

    for word in words:
        wordset.add(word)

wordlist=list(wordset)

countmatrix = np.zeros((sample,len(wordlist)))

for i in range(sample):
    words=word_tokenize(dataset1[i])
    for j in range(len(wordlist)):
        occurence=words.count(wordlist[j])
        countmatrix[i,j]=occurence

np.save('countmatrix.npy',countmatrix)

df = pd.DataFrame(wordlist,columns=['Words'])
df.to_csv('wordlist.csv', index=False)

