from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger

import random
import json

import sys
sys.path.append('~/Cellmon')
import Main_Game

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('cellmon_server.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def create_msg(response):
    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    return message

def handle_request():
    logger.debug(request.form)

    sent_input = str(request.form['Body'])

    CORPUS['Opening'][sent_input] = ['User input']
    with open('chatbot_corpus.json', 'w') as myfile:
        myfile.write(json.dumps(CORPUS, indent=4 ))

    response = "Enter the world of Cellmon? (Y/N)"
    create_msg(response)

    sent_input = str(request.form['Body']).lower()

    if sent_input == 'y':
        Main_Game.start_game()
    elif sent_input == 'n':
        response = "Goodbye."
    else:
        response = "Invalid Input."

    create_msg(response)

    return json_response( status = "ok" ) 
