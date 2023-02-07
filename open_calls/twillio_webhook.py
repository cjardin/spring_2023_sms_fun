import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

from tools.logging import logger

import random

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

with open('my_body.txt', 'r') as myfile:
    all_file = myfile.read()

def handle_request():
    logger.debug(request.form)

    message = g.sms_client.messages.create(
                     body=random.choice(all_file.splitlines()),
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    return json_response( status = "ok" )
