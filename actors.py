from AI_ import AI

class actor:
    def __init__(self, phone_number):
        self.phone = phone_number
        self.prev_msgs = []
        self.name = ''
        self.ai = AI()
        self.state = 'begin'

    def save_msg(self, msg):
        self.prev_msgs.insert(0, msg)
