from classes.processed_text import ProcessedText
from classes.text_generator import TextGenerator
from random import random

class BasicBResponder(TextGenerator):
  def respond(self, in_text: ProcessedText) -> str:
    return self.response
  def rate(self, in_text: ProcessedText) -> float:
    responses = []
    words = in_text.words
    tags = in_text.tags
    if tags == ['NN'] or tags == ['NNP']: #user input is a singular noun
      responses.append((0.00 + random(), "Is a " + words[0] + " all you want to chat about?"))
      responses.append((0.00 + random(), "Wow, I was not expecting a " + words[0]))
      responses.append((0.00 + random(), "Man, I've always wanted a " + words[0]))
    elif tags == ['NNS']: #user input is a plural noun
      responses.append((0.65 + random(), "Are " + words[0] + " all that interest you?"))
      responses.append((0.50 + random(), words[0] + ", " + words[0] + ", " + words[0] + "!!"))
      responses.append((0.70 + random(), "I guess " + words[0] + " are important..."))
    elif tags == ['UH']: #user input is an interjection
      responses.append((0.65 + random(), words[0] + " back at ya!"))
    elif tags == ['PRP', 'VBZ', 'VBG'] and words[0] != 'I':
      responses.append((0.65 + random(), "Why do you think I care?"))
      responses.append((0.65 + random(), "Why " + words[1] + " " + words[0] + " " + words[2]))
    elif tags == ['PRP', 'VBP', 'VBG']: #user input uses progressive verbs
      if words[0] == 'you': #user is talking about chatbot
        responses.appened((0.90 + random(), "mmmm no, you are " + words[2]))
      else: #chatbot is not the subject
        responses.append((0.70, + random(), "Why " + words[1] + " " + words[0] + " " + words[2] + "?"))
    elif tags == ['DT', 'NN', 'VBZ', 'JJ']: #Describing a singular noun
        responses.append((0.70 + random(), "I don't think it's that " + words[3]))
        responses.append((0.70 + random(), words[3] + "?! I disagree!"))
 
    if responses:
      (weight, self.response) = max(responses)
      return weight
    else:
      return float('-inf')
            
