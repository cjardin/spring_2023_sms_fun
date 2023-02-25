from abc import ABC as Abstract, abstractmethod
from typing import List
from classes.processed_text import ProcessedText
from classes.user_data import UserData

class TextProcessor(Abstract):
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

def processors(user_data: UserData) -> List[TextProcessor]:
    return []
