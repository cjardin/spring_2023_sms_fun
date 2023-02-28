#Importing required libraries and tools
import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists

from tools.logging import logger

import json
import pickle

#Get class object from main python file
import sys
sys.path.append('~/Cellmon')
from gameclass_server import *

#Get server info (phone #)
yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

#This function creates the messages to send SMS to user
def create_msg(output):
    for o_msg in output:
        print(o_msg)
        message = g.sms_client.messages.create(
                     body=o_msg,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])

#This function will handle most of the work for the server
def handle_request():
    logger.debug(request.form)  #Debugging tool, can be commented out

    player = None   #Creating an empty player object

    #Checking if the player exists as a pickle file
    if exists(f"users/{request.form['From']}.pkl"):
        with open(f"users/{request.form['From']}.pkl", "rb") as p:
            player = pickle.load(p) #Get user's current state
    else:   #User does not exist, create new player from user's phone #
        player = Player("", request.form['From'], [])

    player.save_msg(request.form['Body'])   #Save user input into player's prev_msgs
    output = player.get_output(request.form['Body'])    #Get the output to send to user

    create_msg(output)  #Send SMS to user

    #If user opted to leave the menu screen, save state as menu
    if player.state == "end" and request.form['Body'].lower() == "exit":
        player.state = "menu"

    #Dump the user's current state and info into pickle file
    with open(f"users/{request.form['From']}.pkl", "wb") as p:
        pickle.dump(player, p)

    return json_response( status = "ok" )   #Return status to server for message
