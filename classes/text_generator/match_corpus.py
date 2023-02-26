import random
from . import TextGenerator
from classes.processed_text import ProcessedText

class MatchCorpus(TextGenerator):
    # TODO: Override `TextGenerator.rate`
    def rate(self, in_text: ProcessedText) -> float:
        from classes.corpus import corpus

        # Try to find a word list in our corpus that matches the user input.
        # TODO: Should make this a distance algorithm instead.
        outputs = corpus.get(in_text.words)
        if outputs: # Doesn't exist, or no options
            self.response = random.choice(outputs)
            return 5.0 # TODO: Reduce weight if used recently?
        else:
            self.response = "NOT FOUND"
            return float("-inf") # Should *never* run, unless the only option

    def respond(self, in_text: ProcessedText) -> str:
        return self.response


