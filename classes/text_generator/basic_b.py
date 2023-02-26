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
    if tags == ['NN'] or tags == ['NNP']:
      responses.append((0.5 + random(), "Is " + words[0] + " all you want to chat about?"))
      responses.append((0.5 + random(), "Wow, a " + words[0] + " sounds really good rn"))
    elif tags == ['NNS']:
      responses.append((0.25 + random(), "Are " + words[0] + " all that interest you?"))
    elif tags == ['UH']:
      responses.append((0.25 + random(), words[0] + " back at ya!"))
    elif tags == ['PRP', 'VBZ', 'VBG'] and words[0] != 'I':
      responses.append((0.25 + random(), "Why do you think I care?"))
      responses.append((0.25 + random(), "Why " + words[1] + " " + words[0] + " " + words[2]))
    if responses:
      (weight, self.response) = max(responses)
      return weight
    else:
      return float('-inf')
            
