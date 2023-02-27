import random
import json

# open corpus json
CORPUS = {}
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def process_message(user, sent_input):

    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input][user.ai.mood])
    else:
        response = random.choice(CORPUS['default']['response'])

    return (user, response)


