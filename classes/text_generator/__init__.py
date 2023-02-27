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

# Import your text generators here.
#
# (Yes, these have to be here; `TextGenerator` has to be defined
# before these derived classes are loaded.)
from . import smile_and_nod
from . import match_corpus
from . import respond_jerk
from . import question_responses
#from . import basic_b

def init_generators(user_data: UserData) -> List[TextGenerator]:
    """Initializes and returns the list of text processors."""

    # These will be checked in order;
    # earlier will win in the rare event of a tie.
    return [
        #basic_b.BasicBResponder(user_data),
        question_responses.responseQuestions(user_data),
        smile_and_nod.SmileAndNod(user_data),
        match_corpus.MatchCorpus(user_data),
        respond_jerk.JerkResponder(user_data),
    ]
