import yaml
from twilio.rest import Client
from flask import g

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

sms_client = None

def get_sms_client():
    global sms_client

    sms_client = client = Client(g.secrets['twilio_account'], g.secrets['twilio_token'])

    return sms_client
