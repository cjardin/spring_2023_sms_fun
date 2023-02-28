import random
from . import TextGenerator
from classes.processed_text import ProcessedText
from difflib import SequenceMatcher 

class MatchCorpus(TextGenerator):
    # TODO: Override `TextGenerator.rate`
    def rate(self, in_text: ProcessedText) -> float:
        from classes.corpus import corpus
        '''
        # Try to find a word list in our corpus that matches the user input.
        # TODO: Should make this a distance algorithm instead.
        outputs = corpus.get(in_text.words)
        if outputs: # Doesn't exist, or no options
            self.response = random.choice(outputs)
            return 5.0 # TODO: Reduce weight if used recently?
        else:
            self.response = "NOT FOUND"
            return float("-inf") # Should *never* run, unless the only option
            '''

        max_percent = 0
        best_output = []
        for response in corpus:
            for inputs in response["inputs"]:
                if max_percent < SequenceMatcher(None, in_text.og_text, inputs).ratio():
                    max_percent = SequenceMatcher(None, in_text.og_text, inputs).ratio()
                    best_output = response["outputs"]

        self.response = best_output[random.randint(0,len(best_output)-1)]

        return max_percent*10
                
            

    def respond(self, in_text: ProcessedText) -> str:
        return self.response
    


