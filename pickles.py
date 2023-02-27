import pickle
from actors import actor
from tools.logging import logger
import os
import json

CORPUS = {}
with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

def pickling(form):
    # pickling
    act = None
    # returning user
    if os.path.exists(f"users/{form['From']}.pkl"):
        with open(f"users/{form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
    # new user
    else:
        act = actor(form['From'])

    # save into message history
    act.save_msg(form['Body'])


    logger.debug(act.prev_msgs)

    return act

# save pickle/user data
def save_pickle(act):
    with open(f"users/{act.phone}.pkl", 'wb') as p:
        pickle.dump(act,p)