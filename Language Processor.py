from nltk import *
from nltk.sentiment import *

test = 'hello there everyone.'
tokens = word_tokenize(test) #Tokenizes the individual words
print(pos_tag(tokens))
tokens = sent_tokenize(test) #Tokenizes the full sentence
print(pos_tag(tokens))
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(test))
