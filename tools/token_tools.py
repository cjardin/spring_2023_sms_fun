import jwt
import datetime
from flask import  g
from tools.logging import logger


def create_token(token_data):
    token_data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30)
    token_data['iat'] = datetime.datetime.utcnow()

    return jwt.encode( token_data , g.secrets['JWT'],  algorithm="HS256")

