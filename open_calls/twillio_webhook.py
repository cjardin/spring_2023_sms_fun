import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

from tools.logging import logger

import sys
sys.path.append('~/Cellmon')
from gameclass_server import *

import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

def create_msg(output):
    for o_msg in output:
        print(o_msg)
        message = g.sms_client.messages.create(
                     body=o_msg,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

#DO NOT RUN SERVER UNTIL READY
def handle_request():
    logger.debug(request.form)

    player = None
    if exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", "rb") as p:
            player = pickle.load(p)
    else:
        player = Player("", request.form['From'], [])

    player.save_msg(request.form['Body'])
    output = player.get_output(request.form['Body'])

    create_msg(output)

    with open(f"users/{request.form['From']}.pkl", "wb") as p:
        pickle.dump(player, p)

    while player.state == "start_game":
        output = player.get_output("")
        create_msg(output)

    return json_response( status = "ok" )
