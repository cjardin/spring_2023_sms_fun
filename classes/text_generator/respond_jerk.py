from random import random
from classes.processed_text import ProcessedText
from classes.text_generator import TextGenerator


# ProcessedText:
# self.words = []
# Important Words
# self.tags = []
# Store lists of words and Penn Treebank tags.
# For more info on the latter, see https://www.sketchengine.eu/penn-treebank-tagset/
# Store the most intense emotion.
# self.intensity

class JerkResponder(TextGenerator):

    def respond(self, in_text: ProcessedText) -> str:
        return self.response

    def rate(self, in_text: ProcessedText) -> float:
        curPos = 0
        responses = []
        # Generate simple responses based on keywords

        for input_word, input_tag in zip(in_text.words, in_text.tags):
            if input_tag == 'VBD':
                responses.append((0.8 + random(), "I " + input_word + " your mom last night"))

            if input_tag == 'NNS':
                responses.append((
                    0.5 + random(),
                    "Man I *love* talking about " + input_word
                ))
                responses.append((
                    0.5 + random(),
                    "Do you really care about " + input_word + "?  That's kinda weird man"
                ))

            if input_tag == 'NN':
                responses.append((
                    0.25 + random(),
                    input_word + "!? A " + input_word + " killed my entire family"))

            curPos += 1

        if responses:
            (weight, self.response) = max(responses)
            return weight
        else:
            return float('-inf')
