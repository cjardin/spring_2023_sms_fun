import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists
from util.actors import actor
from tools.logging import logger
from textblob import TextBlob

import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def fetch_history(from_number):
    act = None
    #Check if phone number has saved history
    if exists( f"users/{from_number}.pkl") :
        with open(f"users/{from_number}.pkl", 'rb') as p:
            act = pickle.load(p)
    else:
        #If no history, start recording
        act= actor(from_number)
    return act

def handle_request():
    # logger.debug(request.form)

    # Refresh JSON for every request
    with open('chatbot_corpus.json', 'r') as myfile:
        CORPUS = json.loads(myfile.read())

    # Fetch conversation history
    act = fetch_history(request.form['From'])

    #Save incoming message to history
    act.save_msg(request.form['Body'])

    logger.debug(act.prev_msgs)

    # Write history to file
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    response = 'NOT FOUND'

    # Sanitize inputs; set to lowercase, strip trailing whitespace
    sent_input = str(request.form['Body']).lower().strip()
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input])
    else:
        try:
            #TODO we need to generate response on a unique input
            blob = TextBlob(sent_input)
            response = "I haven't heard of " + blob.noun_phrases[0] + ", who's in it?"
            CORPUS['input'][sent_input] = [response]
            with open('chatbot_corpus.json', 'w') as myfile:
                myfile.write(json.dumps(CORPUS, indent=4 ))
        except:
            response = "Uhhh, I have no idea what we're talking about. Sorry.."

    logger.debug(response)

    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    return json_response( status = "ok" )
