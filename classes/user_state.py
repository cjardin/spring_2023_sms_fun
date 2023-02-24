from os import path
import pickle
import random
import json
import string

class ChatBot:
    class UserData:
        """Data stored on disk for each user."""

        def __init__(self, phone_number):
            self.prev_msgs = []

        def load(self, save_path: str) -> bool:
            if not path.exists(save_path): return False

            in_file = open(save_path, 'rb')
            loaded = pickle.load(in_file)

            self.prev_msgs = loaded.prev_msgs

            return True

        def save(self, save_path):
            out_file = open(save_path, 'wb')
            pickle.dump(self, out_file)


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

        in_msg = in_msg.lower()
        in_msg = in_msg.translate(str.maketrans('','', string.punctuation)) #removes punctuation to match more in corpus

        # TEMPORARY: This is Prof. Jardin's drag queen bot logic,
        # tweaked to use this class's methods.
        #
        # Feel free to blow this all away to implement actual logic.
        # I suggest adding logic for testing for message features here,
        # and then calling out to other files/functions once we choose
        # an appropriate routine.

        # TODO: Abstract the corpus better (namely into its own class)
        # once we know more about how we want it to work, but no point
        # yet.
        with open('chatbot_corpus.json', 'r') as myfile:
            corpus = json.loads(myfile.read())

        if in_msg in corpus['input']:
            return random.choice(corpus['input'][in_msg])
        else:
            corpus['input'][in_msg] = ['DID NOT FIND']
            with open('chatbot_corpus.json', 'w') as myfile:
                myfile.write(json.dumps(corpus, indent=4))
            return "NOT FOUND"


    def save(self):
        self.user_data.save(self.save_path)
