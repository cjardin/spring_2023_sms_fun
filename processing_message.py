import random
import json

# open corpus json
CORPUS = {}
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def process_message(user, sent_input):
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input])
    else:
        CORPUS['input'][sent_input] = ['DID NOT FIND']
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))

    return response
