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
        responses = []
        # Generate simple responses based on keywords

        for input_word, input_tag in zip(in_text.words, in_text.tags):
            if input_tag == 'VBD':  # Past Tense Verbs
                responses.append((0.30 + random(), "I " + input_word + " your mom last night"))
                responses.append((0.30 + random(), "When was the last time you " + input_word + "?"))

            if input_tag == 'NNS':  # Plural Nouns
                responses.append((0.50 + random(), "Man I *love* talking about " + input_word))
                responses.append((0.50 + random(), "Do you really care about " + input_word + "?  That's kinda weird man"))

            if input_tag == 'NP':  # Proper Nouns
                responses.append((0.50 + random(), "Wait, *the* " + input_word + "?  Holy shit!"))
                responses.append((0.10 + random(), "Yo, didn't " + input_word + "get cancelled?"))
                responses.append((0.25 + random(), input_word + "? From OnlyFans?"))

            if input_tag == 'NNS':  # Present Participle (-ing)
                responses.append((0.30 + random(), input_word + "? Man you're optimistic!"))

            if input_tag == 'NN':  # Singular Nouns
                responses.append((0.25 + random(), input_word + "!? A " + input_word + " killed my entire family"))
                responses.append((0.10 + random(), "Do you really love the " + input_word + " or are you just naming things in the room?"))
                responses.append((0.60 + random(), "Please tell me more about this" + input_word + ".  I am sooo interested -_-"))

            if input_tag == 'JJR':  # Comparative adjectives (-er)
                responses.append((0.55 + random(), input_word + "? I hardly know 'er!"))

            if input_tag == 'JJS':  # Superlative adjectives (-est)
                responses.append((0.25 + random(), "The " + input_word + ", huh?  Have you checked every one?"))

        if responses:
            (weight, self.response) = max(responses)
            return weight
        else:
            return float('-inf')
