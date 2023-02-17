import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)


def send_message(form):
    message = g.sms_client.messages.create(
                     body = '',
                     from_ = yml_configs['twillio']['phone_number'],
                     to = form['From'],
                 )
    return json_response(sid = message.sid)

def send_picture(form, media_url):
    message = g.sms_client.messages.create(
                    from_ = yml_configs['twillio']['phone_number'],
                    media_url = media_url,
                    to = form['From'],
    )
    return json_response(sid = message.sid)


