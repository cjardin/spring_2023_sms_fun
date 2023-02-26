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

        for input_tags in in_text.tags:
            if input_tags == 'VBD':
                responses.append((0.8 + random(), "I " + in_text.words[curPos] + " your mom last night"))

            if input_tags == 'NNS':
                responses.append((0.5 + random(), "Man I *love* talking about " + in_text.words[curPos]))
                responses.append(
                    (0.5 + random(), "Do you really care about " + in_text.words[curPos] + "?  That's kinda weird man"))

            if input_tags == 'NN':
                responses.append((0.25 + random(),
                                  in_text.words[curPos] + "!? A " + in_text.words[curPos] + " killed my entire family"))

            curPos += 1

        # Responses that don't look at the input at all

        responses.append(0.0 + random(), "[EXTREMELY LOUD INCORRECT BUZZER]")
        responses.append(0.0 + random(), "tl;dr")

        self.response = max(responses)[1]
        self.weight = max(responses)[0]

        return self.weight




