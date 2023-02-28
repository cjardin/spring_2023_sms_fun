import random
from . import TextGenerator
from classes.processed_text import ProcessedText
from difflib import SequenceMatcher 

class MatchCorpus(TextGenerator):

    def rate(self, in_text: ProcessedText) -> float:
        from classes.corpus import corpus

        max_percent = 0
        best_output = []
        for response in corpus:
            for inputs in response["inputs"]:
                if max_percent < SequenceMatcher(None, in_text.og_text, inputs).ratio():
                    max_percent = SequenceMatcher(None, in_text.og_text, inputs).ratio()
                    best_output = response["outputs"]

        self.response = best_output[random.randint(0,len(best_output)-1)]

        # return max_percent * 10

        if max_percent > 0.70:
            return 10
        else:
            return 0
                
            

    def respond(self, in_text: ProcessedText) -> str:
        return self.response
    


