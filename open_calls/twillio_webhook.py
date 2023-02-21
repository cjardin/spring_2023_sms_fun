import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger
from pickles import pickling
from send_message_back import send_message, send_picture
from processing_message import process_message

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

### Main
def handle_request():
    # user info
    #logger.debug(request.form)
    logger.debug(request.form['From'])

    # pickling from pickles.py
    pickling(request.form)

    ### processing incoming message from processing_message.py w corpus
    sent_input = str(request.form['Body']).lower()
    test_response = process_message(sent_input) # this should be response aka `response = process_message(sent_input)`
    logger.debug(test_response)

    ### response back
    response = "Insert Response Here"
    logger.debug(response)
    # sending back message from send_message_back.py
    # send message 
    send_message(request.form, response)
    # send picture name/url from media.yml
    picture_name = "catfish-image"
    send_picture(request.form, picture_name)
    
    
    return json_response( status = "ok" )
