import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger

import random
import json

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

    response = "Enter the world of Cellmon? (Y/N)"
    create_msg(response)

    sent_input = str(request.form['Body']).lower()

    if sent_input == 'y':
        with open("~/Cellmon/Main_Game.py") as game:
            exec(game)
    elif sent_input == 'n':
        response = "Goodbye."
    else:
        response = "Invalid Input."
    
    create_msg(response)

    return json_response( status = "ok" )
