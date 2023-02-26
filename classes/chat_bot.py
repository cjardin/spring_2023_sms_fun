from classes.user_data      import UserData
from classes.processed_text import ProcessedText
from classes.text_generator import init_generators
from classes.corpus         import corpus

class ChatBot:
    def __init__(self, phone_number):
        """
        Attempts to load the user's data from disk;
        default-initializes if it doesn't exist.
        """

        self.phone = phone_number
        self.save_path = f"users/{self.phone}.pkl"

        self.user_data = UserData(phone_number)
        self.user_data.load(self.save_path)

        self.generators = init_generators(self.user_data)

    def __del__(self):
        """Destructor; writes data to disk."""
        self.save()

    # Utilities

    def is_loaded(self) -> bool:
        self.prev_msgs is not None

    def push_history(self, in_msg: str):
        self.user_data.prev_msgs.append(in_msg)

    # Primary methods

    def run(self, in_msg: str) -> str:
        """Executes the chatbot for one input message. Returns our reply."""

        # Reload the corpus, so we can edit it at runtime!
        corpus.reload()

        proc_text = ProcessedText(in_msg)

        # Choose the text generator that reports the highest rating.
        best_gen = self.generators[0]
        best_rating = best_gen.rate(proc_text)
        for gen in self.generators[1:]:
            rating = gen.rate(proc_text)
            if rating > best_rating:
                best_rating = rating
                best_gen = gen

        # Allow the best match to generate our response.
        return best_gen.respond(proc_text)

    def save(self):
        self.user_data.save(self.save_path)
