class Player:
    def __init__(self, username, phone_number):
        self.username = username
        self.phone = phone_number
        self.role = None
        
    def vote(opinion):
        print("I vote for:", opinion)
        
    def assign_role(self, role):
        self.role = role
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_phone(self):
        return self.phone

    
class Doctor(Player):
    pass

class Police(Player):
    pass

class Warewolf(Player):
    pass

class Moderator(Player):
    def welcome():
        return "Welcome to the mafia game, in this blah blah"
    
    def vote_to_kill(player, players_left):
        return "Player (%s) has been killed, there are %d players left." % (player, players_left))"
    

