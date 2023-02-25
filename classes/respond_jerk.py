from random import random
from classes.processed_text import ProcessedText


# ProcessedText:
# self.words = []
# Important Words
# self.tags = []
# Store lists of words and Penn Treebank tags.
# For more info on the latter, see https://www.sketchengine.eu/penn-treebank-tagset/
# Store the most intense emotion.
# self.intensity

class JerkResponder:
    def __init__(self):
        self.curPos = 0
        # Current word being processed
        self.repeatWeight = 0
        # Unimplemented for now, idea is to reduce weight on repeated formats

    def generate_insult(self, input_text: ProcessedText, responses):

        # Generate responses based on keywords

        for input_tags in input_text .tags:
            if input_tags == 'VBD':
                responses.append(0.8 + random() - self.repeatWeight, "I " + input_text.words[self.curPos] + " your mom last night")

            if input_tags == 'NNS':
                responses.append((0.5 + random() - self.repeatWeight, "Man I *love* talking about " + input_text.words[self.curPos]))
                responses.append((0.5 + random() - self.repeatWeight, "Do you really care about " + input_text.words[self.curPos] + "?  That's kinda weird man"))

            if input_tags == 'NN':
                responses.append((0.25 + random() - self.repeatWeight, input_text.words[self.curPos] + "!? A " + input_text.words[self.curPos] + " killed my entire family"))

            self.curPos += 1

        # Responses that don't look at the input at all

        self.responses.append(0.0 + random() - self.repeatWeight, "[EXTREMELY LOUD INCORRECT BUZZER]")
        self.responses.append(0.0 + random() - self.repeatWeight, "tl;dr")
