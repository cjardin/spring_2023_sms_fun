import os, queue, random

#needs to to not show number, just show username

def get_filenames(path):
    return os.listdir(path)

def waiting_room():
    
    ready_lobby = queue.Queue()
    
    players_list = get_filenames()
    
    while(players_list < 3 ):
        for player in players_list:
            if player not in ready_lobby:
                ready_lobby.put(player)
                print(f"player {player} joined the game")
            
            #starts game after 3 players join, (always as the contrario), change later for a command
            if len(ready_lobby > 3):
                assign_roles(ready_lobby)
            else:
                print(f"Waiting for {len - 3} more players")
            

def assign_roles(player_list):
    for phone_number in player_list:
        print('temp')