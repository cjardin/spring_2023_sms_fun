#import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

input_sen = 'I Hate COVID'
print(input_sen)
print(sia.polarity_scores(input_sen))

tokens = nltk.word_tokenize(input_sen)

