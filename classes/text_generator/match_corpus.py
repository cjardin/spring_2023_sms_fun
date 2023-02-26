import random
import json
from . import TextGenerator
from classes.processed_text import ProcessedText

class MatchCorpus(TextGenerator):
    # TODO: Override `TextGenerator.rate`
    def rate(self, in_text: ProcessedText) -> float:
        # TODO: Abstract the corpus better (namely into its own class)
        # once we know more about how we want it to work, but no point yet.
        with open('chatbot_corpus.json', 'r') as corpus_in:
            corpus = json.loads(corpus_in.read())

        # Try to find a word list in our corpus that matches the user input.
        # TODO: Should make this a distance algorithm instead.
        outputs = None
        for resp in corpus['responses']:
            if resp['input'] != in_text.words: continue
            outputs = resp['outputs']
            break

        if outputs: # Doesn't exist, or no options
            self.response = random.choice(outputs)
            return 5.0 # TODO: Reduce weight if used recently?
        else:
            if in_text.words and outputs is None:
                # Add the input to the corpus.
                corpus['responses'].append({
                    "input": in_text.words,
                    "outputs": []
                })
                corpus_out = open('chatbot_corpus.json', 'w')
                corpus_out.write(json.dumps(corpus, indent=4))

            self.response = "NOT FOUND"
            return float("-inf") # Should *never* run, unless the only option

    def respond(self, in_text: ProcessedText) -> str:
        return self.response


