import random;
from ntlmod import analyzeSentiment 
from processing_message import *

class AI:
    
    def __init__(self):
        #self.mood = random.choice(['HAPPY', 'SAD', 'ANGRY', 'NEUTRAL'])
        self.STRESS_LEVEL = 0 #global incrementor
        self.mood = 'neutral'
        self.mood_value = 0
        
    #return whatever mood (strgin the AI is feeling)
    def update_mood_value(self, compound):
        self.mood_value += compound
        #return self.mood_value
    
    #TODO: Fix algorithm to set the mood once we can determine the percentajes
    def setMood(self):
        if self.compound > .2:
            self.mood = 'happy'
        elif self.compound == 0:
            self.mood = 'neutral'
        elif self.compound < (-.2):
            self.mood = 'mad'

    #! NOT WORKING, NEEDS TO FIX OVERALL STRESS LEVEL
    def getStressLevel(self):
        return self.STRESS_LEVEL
    
    #returns current message being processed, for debugging porpuses
    def isTheCurrentMessage(self):
        return self.incoming_message

    #recieves user input and deconstructs ther analyzeSentiment
    #cureently string and float variables are not being used
    #sets the mood
    #TODO: need to fix algorith that takes overall messages and send it to determine the mood
    def clientInput(self, incoming_message):
        self.incoming_message = incoming_message
        string, sentiment_value, float_value = analyzeSentiment(self.incoming_message)
        compound = sentiment_value['compound']
        print(sentiment_value['compound'])
        self.update_mood_value(compound)
        #self.setMood(self.mood, sentiment_value['compound'])

    #temp function
    def response(self):
        pass
