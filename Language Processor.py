from nltk import *
from nltk.sentiment import *
from nltk.corpus import stopwords #This is to give us a corpus of stopwords
#from nltk.stem import PorterStemmer #This will remove any sort of suffixes to the word


test = 'A cat was running around the house last night for some odd reason.'
stopWords = set(stopwords.words('english')) #Building a list of stop words
words = word_tokenize(test)
wordsFiltered = []

for w in words: #Goes through our list of words
    if w not in stopWords: #See if they are not a stop word
        wordsFiltered.append(w) #If not, append to the list

print(wordsFiltered)#This shows all words that were NOT stopwords
tokens = word_tokenize(test) #Tokenizes the individual words
print(pos_tag(tokens))
tokens = sent_tokenize(test) #Tokenizes the full sentence
print(pos_tag(tokens))
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(test))
