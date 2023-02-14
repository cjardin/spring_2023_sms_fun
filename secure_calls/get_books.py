from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from tools.logging import logger

def handle_request():
    logger.debug("Get Books Handle Request")
    logger.debug(request.args)

    return json_response( token = create_token(  g.jwt_data ) , books = {})

