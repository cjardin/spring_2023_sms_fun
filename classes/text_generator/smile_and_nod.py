from . import TextGenerator
from classes.processed_text import ProcessedText
import random

class SmileAndNod(TextGenerator):
    """
    Fallback text generator, in case we're really at a loss.
    Doesn't care about user input; just dismisses whatever
    they have to say.
    """

    # The default `__init__` should be everything we need.
    # General rule: don't override it unless you're sure
    # you should.

    def rate(self, in_text: ProcessedText) -> float:
        # Arbitrarily low, but not -∞.
        return 0

    def respond(self, in_text: ProcessedText) -> str:
        phrases = open("data/fallback_phrases.txt", 'r')
        return random.choice(list(phrases.readlines()))
