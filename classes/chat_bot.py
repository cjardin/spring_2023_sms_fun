import random
import json
from classes.processed_text import ProcessedText
from tools.logging import logger

class ChatBot:
    def __init__(self, phone_number):
        """
        Attempts to load the user's data from disk;
        default-initializes if it doesn't exist.
        """

        self.phone = phone_number
        self.save_path = f"users/{self.phone}.pkl"
        self.user_data = self.UserData(phone_number)

        self.user_data.load(self.save_path)


    def __del__(self):
        """Writes data to disk when this object is freed."""
        self.save()

    # Utilities

    def is_loaded(self) -> bool:
        self.prev_msgs is not None

    def push_history(self, in_msg: str):
        self.user_data.prev_msgs.append(in_msg)

    # Primary methods

    def run(self, in_msg: str) -> str:
        """Executes the chatbot for one input message. Returns our reply."""

        proc_text = ProcessedText(in_msg)

        # TODO: Abstract the corpus better (namely into its own class)
        # once we know more about how we want it to work, but no point yet.
        with open('chatbot_corpus.json', 'r') as corpus_in:
            corpus = json.loads(corpus_in.read())

        # Try to find a word list in our corpus that matches the user input.
        # TODO: Should make this a distance algorithm instead.
        outputs = None
        for resp in corpus['responses']:
            if resp['input'] != proc_text.words: continue
            outputs = resp['outputs']
            break

        logger.debug(proc_text.words)

        if outputs:
            return random.choice(outputs)
        else:
            # Add the input to the corpus.
            corpus['responses'].append({
                "input": proc_text.words,
                "outputs": ["DID NOT FIND"]
            })
            corpus_out = open('chatbot_corpus.json', 'w')
            corpus_out.write(json.dumps(corpus, indent=4))
            return "NOT FOUND"


    def save(self):
        self.user_data.save(self.save_path)
