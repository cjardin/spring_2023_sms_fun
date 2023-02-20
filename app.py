#!/home/ubuntu/anaconda3/bin/python3
from flask import Flask, redirect, g, make_response

import traceback

from tools.secrets import get_secrets
from tools.twilio import get_sms_client

from tools.logging import logger
from bin.twilio_webhook import handle_request

#Create our app
app = Flask(__name__)

# Redirect requests that don't specify a page to our index page.
@app.route('/')
def index():
    return redirect('/static/index.html')

@app.route("/open_api/twillio_webhook", methods = ['POST'])
def twilio_webhook():
    logger.debug("Call to twilio_webhook")

    #g is flask for a global var storage
    g.secrets = get_secrets()
    g.sms_client = get_sms_client()

    try:
        response, code = handle_request()
    except Exception as err:
        ex_data = str(Exception) + '\n'
        ex_data = ex_data + str(err) + '\n'
        ex_data = ex_data + traceback.format_exc()
        logger.error(ex_data)
        response = 'Internal server error'
        code = 500

    return make_response(response, code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

