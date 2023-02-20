from nltk import *
from nltk.sentiment import *
from nltk.corpus import stopwords #This is to give us a corpus of stopwords
from nltk.stem import PorterStemmer #This will remove any sort of suffixes to the word
from nltk.corpus import wordnet #This will give us snynoms and antnyoms of words


#stopWords = set(stopwords.words('english')) #Building a list of stop words
#words = word_tokenize(test)
#wordsFiltered = []

#for w in words: #Goes through our list of words
 #   if w not in stopWords: #See if they are not a stop word
  #      wordsFiltered.append(w) #If not, append to the list

#print(wordsFiltered)#This shows all words that were NOT stopwords


#tokens = word_tokenize(test) #Tokenizes the individual words
#print(pos_tag(tokens))


#tokens = sent_tokenize(test) #Tokenizes the full sentence
#print(pos_tag(tokens))


#sia = SentimentIntensityAnalyzer() #VADER instance
#print(sia.polarity_scores(test)) #Using the VADER instance to judge intent


def remove_filler (raw_text):
    stopWords = set(stopwords.words('english')) #Building a list of stop words
    words = word_tokenize(raw_text) #Gets a list of all individual words in the raw input text string
    wordsFiltered = [] #Will store all the non-stop words
    stemmer = PorterStemmer() #Gets an instance of the stemming function

    for w in words: #Goes through our list of words
        if w not in stopWords: #See if they are not a stop word
            w = stemmer.stem(w) #Get the base stem of the word
            wordsFiltered.append(w) #If not, append to the list

    return wordsFiltered



test = "I really love to kill ghosts"
print (remove_filler(test))
