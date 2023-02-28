import nltk

# leave instructions incase server needs to download
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyzeSentiment(string):

    sia = SentimentIntensityAnalyzer()
    #print(sia.polarity_scores('Wow. NLTK IS SICK!'))
    polarity = sia.polarity_scores(string)
    pos= nltk.pos_tag(nltk.word_tokenize(string))

    return string, polarity, pos
