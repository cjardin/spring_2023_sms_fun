import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.logging import logger
from pickles import pickling, save_pickle
from send_message_back import send_message, send_picture
from processing_message import process_message
### Main
def handle_request():
    # user info
    #logger.debug(request.form)
    logger.debug(f"Phone#: {request.form['From']}")

    # pickling from pickles.py
    user = pickling(request.form)

    ### processing incoming message from processing_message.py
    sent_input = str(request.form['Body']).lower()
    
    logger.debug(f"Text: {request.form['Body']}")
    user, response = process_message(user, sent_input)
    
    ### response back
    # sending back message from send_message_back.py
    # send message 
    send_message(user.phone, response)
    # send picture name/url from media.yml
    #picture_name = "catfish-image"
    #send_picture(request.form, picture_name)
    
    # save pickle/user
    save_pickle(user)
    
    return json_response( status = "ok" )
