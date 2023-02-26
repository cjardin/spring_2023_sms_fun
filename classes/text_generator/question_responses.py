from . import TextGenerator
from classes.processed_text import ProcessedText
import random

class reponse_question(TextGenerator):
    """
    Fallback text generator, in case we're really at a loss.
    Doesn't care about user input; just dismisses whatever
    they have to say.
    """

    # The default `__init__` should be everything we need.a
    # General rule: don't override it unless you're sure
    # you should.

    def rate(self, in_text: ProcessedText) -> float:
        # Arbitrarily low, but not -∞.
        if (in_text.og_text[in_text.og_text.length()-1] == '?'):
        return 9.0
    ## FIX THIS WITH SMARTER THINKING

    def respond(self, in_text: ProcessedText) -> str:
        responses = []
        dont_use["who","what", "where", "when", "how", "why"]
        i = random.randint(1,in_text.words.length()-1)
        for word, tag in zip (in_text.words, in_text.tags):
            if (word is not in dont_use):
                if "who" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "what" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "where" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "when" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "why" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "how" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                elif "will" is in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NNS':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    elif input_tag == 'NN':
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                    else:
                else:
                    responses.append("Who...? Who asked?")
                    
