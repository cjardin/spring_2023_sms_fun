from abc import ABC as Abstract, abstractmethod
from typing import List
from classes.processed_text import ProcessedText
from classes.user_data import UserData

class TextGenerator(Abstract):
    """
    Base class for a text-processing algorithm.

    @field user_data: a reference to the current user's data.
    Use it to store persistent data for your algorithm.
    """
    def __init__(self, user_data: UserData):
        self.user_data = user_data # Save a reference for later.

    def rate(self, in_text: ProcessedText) -> float:
        """
        Called on each `TextProcessor`. Returns a number describing
        how well-suited this algorithm is to the input text.
        """
        return 1.0

    @abstractmethod
    def respond(self, in_text: ProcessedText) -> str:
        """
        Called when this processor has been chosen.
        Returns the reply to `in_text`.
        """
        pass

# Yes, these imports have to be down here, or else the program
# will fail due to circular imports.
from . import match_corpus

def init_generators(user_data: UserData) -> List[TextGenerator]:
    """Initializes and returns the list of text processors."""
    return [
        match_corpus.MatchCorpus(user_data)
    ]
