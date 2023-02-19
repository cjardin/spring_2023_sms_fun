class Actor:
    def __init__(self,phone_number, name, role):
        self.phone = phone_number
        self.prev_msgs=[]
        self.name = name
        self.role = role
    def save_msg(self,msgs):
        self.prev_msgs.append(msgs)

class MafiaGame:
    def __init__(self, players):
        self.players = [Actor(player, None) for player in players]
        
    def assign_roles(self):
        number_of_mafiosos = len(self.players) // 3
        for i in range(number_of_mafiosos):
            self.players[i].role = "Mafioso"
        for i in range(number_of_mafiosos, len(self.players)):
            self.players[i].role = "Innocent"
            
    def show_roles(self):
        for player in self.players:
            print(f"{player.name} is a {player.role}")

players = [""]
players.append(Actor.name)
#game = MafiaGame(players)
#game.assign_roles()
#game.show_roles()
   
