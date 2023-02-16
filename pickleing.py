import pickle
from actors import actor
from tools.logging import logger
import os

def pickling(form):
    # pickling
    act = None
    if os.path.exists(f"users/{form['From']}.pkl"):
        with open(f"users/{form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
    else:
        act = actor(form['From'])
    act.save_msg(form['Body'])
    logger.debug(act.prev_msgs)
    with open(f"users/{form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)