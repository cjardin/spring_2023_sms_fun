import json
from typing import List, Optional
from classes.processed_text import ProcessedText

# Don't construct new instances of this; import the single `corpus` at
# the bottom of this module instead.
class Corpus:
    def __init__(self):
        self.reload()

    def __del__(self):
        self.save()

    def __iter__(self):
        return iter(self.body['responses'])

    def reload(self):
        self.dirty = False
        file_in = open('chatbot_corpus.json', 'r')
        self.body = json.loads(file_in.read())

    def get(self, in_words: List[str]) -> Optional[List[str]]:
        """
        Returns the list of responses if a match for `in_words` is found,
        otherwise returns `None`.

        Keep in mind that this is O(m•n), where m is the number of entries
        in the corpus and n is the length of the longest entry. If you are
        looking for multiple entries, then you might want a different search
        strategy.

        (Don't spend too long thinking about if this use of big-O notation
        is correct; it's probably not, but I think you get the point.)
        """
        for responses in self:
            for an_input in responses['inputs']:
                if an_input.split(" ") == in_words:
                    return responses['outputs']

    def save(self):
        if not self.dirty: return
        self.dirty = False
        corpus_out = open('chatbot_corpus.json', 'w')
        corpus_out.write(json.dumps(self.body, indent=4))

    def append(self, in_text: ProcessedText, outputs: List[str]):
        self.dirty = True
        self.body['responses'].append({
            "input": ' '.join(in_text.words),
            "outputs": outputs,
            "auto_generated": True, # Not checked; just a note to human readers
        })

# Import me!
corpus = Corpus()
