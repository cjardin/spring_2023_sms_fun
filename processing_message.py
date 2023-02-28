import random
import json
import difflib

# open corpus json
CORPUS = {}
CORPUS_RESPONSES = []
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())
    CORPUS_RESPONSES = [response.lower() for response in CORPUS.keys()]


def process_message(user, sent_input):
    best_match = difflib.get_close_matches(sent_input, CORPUS_RESPONSES, n=1, cutoff=0.2)

    if best_match:
        print(best_match)
        response = CORPUS[best_match[0]]
    else:
        response = CORPUS['default']

    """
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input][user.ai.mood])
    else:
        response = random.choice(CORPUS['default']['response'])
    """

    return (user, response)


