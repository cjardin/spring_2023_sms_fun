from classes.processed_text import ProcessedText
from classes.respond_jerk import JerkResponder

# ProcessedText:
# self.words = []
# Important Words
# self.tags = []
# Store lists of words and Penn Treebank tags.
# For more info on the latter, see https://www.sketchengine.eu/penn-treebank-tagset/
# Store the most intense emotion.
# self.intensity


class ResponseManager:

    def __init__(self, text_to_process: ProcessedText):
        self.input = text_to_process;
        self.responses = []  # List of tuples with a possible response and quality weight

    def generate_responses(self):
        # Each response generator is called, and it adds its ideas to the list of tuples, formatted (weight, response)

        JerkResponder.generate_insult(self.input, self.responses)

        # Highest rated response at the end of the process is returned

        result = max(self.responses)
        return result[1]
