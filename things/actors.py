import json

MY_GAME_LOGIC = {}
with open('college_trail.json', 'r') as myfile:
    MY_GAME_LOGIC = json.loads(myfile.read())


class actor:
    def __init__(self, phone_number):
        self.phone = phone_number
        self.prev_msgs = []
        self.state = "init"

    def save_msg(self, msg):
        self.prev_msgs.append(msg)
