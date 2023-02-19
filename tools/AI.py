import random;

class AI:
    def __init__(self):
        self.mood = ['Happy', 'Sad', 'Angry', 'Neutral']
        
    def get_mood(self):
        return random.choice(self.mood)
    