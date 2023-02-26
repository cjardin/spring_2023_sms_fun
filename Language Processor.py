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


def give_context (raw_text):

    #context = [] #This wil store all the meaningful context
    
    stopWords = set(stopwords.words('english')) #Building a list of stop words
    words = word_tokenize(raw_text) #Gets a list of all individual words in the raw input text string
    wordsFiltered = "" #Will store all the non-stop words
    stemmer = PorterStemmer() #Gets an instance of the stemming function

    sia = SentimentIntensityAnalyzer() #Instance of Vader
    sia = max(sia.polarity_scores(raw_text)) #Gets the most prominent emotion.

    #context.append(sia)

    for w in words: #Goes through our list of words
        if w not in stopWords: #See if they are not a stop word
            wordsFiltered = wordsFiltered + " " + w  #If not, append to the list

    #context.append(wordsFiltered)

    raw_tags_stored = "" #Will store all tags
    tagged = word_tokenize(raw_text)#Tokenize the filtered list
    tagged = pos_tag(tagged)#Tag the list
    for tags in tagged:
        raw_tags_stored = raw_tags_stored + " " + tags[1] #Stores tags into a string that directly matches the stemmed words
        
    tags_stored = "" #Will store all tags
    tagged = word_tokenize(wordsFiltered)#Tokenize the filtered list
    tagged = pos_tag(tagged)#Tag the list
    for tags in tagged:
        tags_stored = tags_stored + " " + tags[1] #Stores tags into a string that directly matches the stemmed words


    context = [] #This wil store all the meaningful context
    context.append(raw_text)#The first element in the list is the orginal string.
    context.append(raw_tags_stored)
    context.append(sia) #The second element in the list is the VADER response of the string
    context.append(wordsFiltered)#The third element in the list is a string with all stop words removed.
    context.append(tags_stored) #The fourth element in the list is a string of all the types of speech/tags of the non-stop words [PATTERNS]
    return context 



print ("Please type a sentence to find out what the context is [DEBUGGING PURPOSES ONLY]")
print ("Type: exit() when finished")
text = ""
while (1):
    text = input("> ")
    if (text == "exit()"):
        break
    print(give_context(text))
    
    
    

