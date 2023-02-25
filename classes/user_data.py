from os import path
import pickle

class UserData:
    """The data stored on disk for each user."""

    def __init__(self, phone_number):
        self.prev_msgs = []

    def load(self, save_path: str) -> bool:
        if not path.exists(save_path): return False

        in_file = open(save_path, 'rb')
        loaded = pickle.load(in_file)

        self.prev_msgs = loaded.prev_msgs

        return True

    def save(self, save_path):
        out_file = open(save_path, 'wb')
        pickle.dump(self, out_file)

