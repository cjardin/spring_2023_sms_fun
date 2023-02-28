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
        return self.response[0].upper() + self.response[1:]

    def rate(self, in_text: ProcessedText) -> float:
        responses = []
        # Generate simple responses based on keywords

        for input_word, input_tag in zip(in_text.words, in_text.tags):

            if input_word == "i":  # User talking about self
                responses.append((0.70 + random(), "You talk about yourself a lot"))
                responses.append((0.70 + random(), "Yawn, can we talk about something other than you?"))
                responses.append((0.70 + random(), "Can we talk about something other than you?"))
                responses.append((0.70 + random(), "Do you always talk about yourself this much?"))
                responses.append((0.70 + random(), "It's cute that you think I care about what you"))

            if input_word == "you":  # User talking about bot
                responses.append((0.70 + random(), "Don't talk about me like you know me"))
                responses.append((0.70 + random(), "Yes, that's *totally* me"))
                responses.append((0.70 + random(), "Sounds like me"))
                responses.append((0.70 + random(), "Is that really what you think of me?"))
                responses.append((0.70 + random(), "I am sad you think that about me"))
                responses.append((0.70 + random(), "I am happy you think that about me"))
                responses.append((0.70 + random(), "I am *so* happy you think that about me"))

            if input_tag == 'VBD':  # Past Tense Verbs
                responses.append((0.40 + random(), "I " + input_word + " your mom last night"))
                responses.append((0.50 + random(), "When was the last time you " + input_word + "?"))

            if input_tag == 'JJ':  # Adjectives
                responses.append((0.50 + random(), "How " + input_word + "?"))
                responses.append((0.50 + random(), "Like, really " + input_word + "?"))

            if input_tag == 'VBP' and input_word != "do" and input_word != "are" and input_word != "am":  # Present Tense Verbs
                responses.append((0.40 + random(), "I " + input_word + " once.  Wouldn't recommend it."))
                responses.append((0.40 + random(), "Do you " + input_word + " often?"))
                responses.append((0.40 + random(), "Do you " + input_word + " a lot? o_O"))
                responses.append((0.40 + random(), "When do you think you'll " + input_word + " next?"))


            if input_tag == 'NN' and input_word != "hello":  # Singular Nouns
                responses.append((0.00 + random(), input_word + "!? A " + input_word + " killed my entire family"))
                # responses.append((0.00 + random(), "Do you really love the " + input_word + " or are you just naming things in the room?"))
                responses.append((0.00 + random(), "Please tell me more about this " + input_word + ".  I am sooo interested -_-"))
                responses.append((0.00 + random(), "So, you mentioned " + input_word + ".  Could you tell me more about that?"))
                responses.append((0.00 + random(), "So, about this " + input_word + ".  Tell me more about that!"))
                # responses.append((0.00 + random(), "Don't worry about " + input_word + ".  Let me worry about " + input_word + "!"))
                # responses.append((0.00 + random(), input_word + "? At this time of year, at this time of day, in this part of the country, localized entirely within your kitchen?!"))
            

            if input_tag == 'NNS':  # Plural Nouns
                responses.append((0.00 + random(), "Man I *love* talking about " + input_word))
                responses.append((0.00 + random(), "Do you really care about " + input_word + "?  That's kinda weird man"))
                responses.append((0.00 + random(), "So, about these " + input_word + ".  Tell me more about them"))
                responses.append((0.00 + random(), "Are " + input_word + " really all you ever talk about?"))
                responses.append((0.00 + random(), "Sorry, random question, but this is in my head and I gotta ask, "
                                                   "you know how a group of dolphins is called a pod, what are a "
                                                   "group of " + input_word + " called?"))


            if input_tag == 'NNP':  # Proper Nouns
                responses.append((0.50 + random(), "Wait, *the* " + input_word + "?  Holy shit!"))
                responses.append((0.50 + random(), "Yo, didn't " + input_word + "get cancelled?"))
                responses.append((0.50 + random(), input_word + "? From OnlyFans?"))

            if input_tag == 'VBG':  # Present Participle (-ing)
                responses.append((0.60 + random(), input_word + "? Man you're optimistic!"))

            if input_tag == 'JJR':  # Comparative adjectives (-er)
                responses.append((0.65 + random(), "They aren't " + input_word + " than me"))

            if input_tag == 'JJS':  # Superlative adjectives (-est)
                responses.append((0.45 + random(), "The " + input_word + ", huh?  Have you checked every one?"))

        if responses:
            (weight, self.response) = max(responses)
            return weight
        else:
            return float('-inf')
