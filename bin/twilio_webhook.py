from flask import request, g#ravity?

from tools.logging import logger
from classes.chat_bot import ChatBot
from tools.config import yml_configs

def handle_request():
    logger.debug(request.form)

    phone_num = request.form['From']

    bot = ChatBot(phone_num)
    out_msg = bot.run(request.form['Body'])
    logger.debug(out_msg)

    g.sms_client.messages.create(
        body=out_msg,
        from_=yml_configs['twillio']['phone_number'],
        to=request.form['From'])

    return "OK", 200
