#Importing required libraries
import random
import json
import sys
sys.path.append('open_calls')
from twillio_webhook import *

win, lose, flee = False, False, False

GAME_LOGIC = {}
with open('cellmon_server.json', 'r') as file:
    GAME_LOGIC = json.loads(file.read())

#Defines the user's class for the game (name, phone #, and cellmon party)
class Player:
    def __init__(user, name, number, party):
        user.name = name
        user.number = number
        user.party = party[:2]
        user.prev_msgs = []
        user.state = "init"
        user.currentEnemy = None

    def save_msg(user, msg):
        user.prev_msgs.append(msg)

    def get_output(user, msg_input):
        mob = None
        response = []
        global win, lose, flee
        win, lose, flee = False, False, False
        found_match = False
        output = []

        if 'next_state' not in GAME_LOGIC[ user.state ]:    #Game has ended
            output.append(GAME_LOGIC[ user.state ]['content'])
            return output

        if type(GAME_LOGIC[ user.state ]['next_state']) != str:     #User input (states: enter_choose, choose_Starter, menu, partyTime, explore, battle_menu)
            for next_state in GAME_LOGIC[ user.state ]['next_state']:
                if msg_input.lower() ==  next_state['input'].lower():
                    user.state = next_state['next_state']
                    found_match = True
                    break

            if found_match == False:
                return ['Invalid input.']

        if user.state == "wait_name":
            output.append(f"Welcome {msg_input}!")
            user.name = msg_input
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "getStarter":
            if msg_input.lower() == "terrasaur":
                user.party.append(Starter1)
            elif msg_input.lower() == "jellyfists":
                user.party.append(Starter2)
            elif msg_input.lower() == "fiamelon":
                user.party.append(Starter3)
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "explore":
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "partyTime":
            output.append(GAME_LOGIC[ user.state ]['content'])
            output.extend(playerparty(user))
        elif user.state == "display":
            num = int(msg_input) - 1
            output.append(user.party[num].printMaxStats())
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
            output.extend(playerparty(user))
        elif user.state == "battle_init":
            response, user.currentEnemy = Cellsearch(user, msg_input.lower())
            output.append(response)
            output.append(f"{user.name} sent out {user.party[0].species}!")
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "attack" or user.state == "spAttack":
            speed = checkSpeed(user.party[0], user.currentEnemy)
            response, win, lose = attackMob(user, user.currentEnemy, speed, user.state)
            output.extend(response)
            if lose is False and win is False:
                if speed == 1:
                    speed = 0
                else:
                    speed = 1
                response, win, lose = attackMob(user, user.currentEnemy, speed, user.state)
                output.extend(response)
                user.state = GAME_LOGIC[ user.state ]['next_state']
                output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "stats":
            output.append(f"Printing stats:\n{user.name}'s Current Cellmon\n")
            output.append(user.party[0].printMaxStats())
            output.append("\nEnemy\n")
            output.append(user.currentEnemy.printMaxStats())
            user.state = GAME_LOGIC[ user.state ]['next_state']
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "capture":
            response, win = captureMob(user, user.currentEnemy)
            output.append(response)
            if win is False:
                user.state = GAME_LOGIC[ user.state ]['next_state']
                output.append(GAME_LOGIC[ user.state ]['content'])
        elif user.state == "flee":
            response, flee = fleeBattle(user)
            output.append(response)
            if flee is False:
                user.state = GAME_LOGIC[ user.state ]['next_state']
                output.append(GAME_LOGIC[ user.state ]['content'])
        else:
            output.append(GAME_LOGIC[ user.state ]['content'])

        if win is True:
            output.append(f"{user.name} has won the battle!\nLooks like your cellmon have gained some levels!")
            for mon in user.party: #Loop through player's party and level up each cellmon
                if mon != user.currentEnemy: #Recently caught enemy mob will not be leveled up
                    mon.level_up()
                    mon.currentHP = mon.maxHP
                    output.append(mon.printMaxStats())
            user.state = "menu"
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif lose is True:
            user.state = "end"
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif flee is True:
            user.state = "menu"
            output.append(GAME_LOGIC[ user.state ]['content'])
        elif msg_input.lower() == "exit":
            return output
        elif type(GAME_LOGIC[ user.state ]['next_state']) == str:
            user.state = GAME_LOGIC[ user.state ]['next_state']

        return output

#Defines the main class of the mobs (species, level, stats)
class Cellmon:
    def __init__(self, level, baseHP=0, baseAttack=0, baseSpAttack=0, baseDefense=0, baseSpDef=0, baseSpeed=0,
                 starterHP=0, starterAttack=0, starterSpAttack=0, starterDef=0, starterSpDef=0, starterSpeed=0,
                 species="Cellmon"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level=level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

    #Copy function to add a new cellmon to the user's party
    def Cellcapture(self):
        new = Cellmon(1)
        new.species = self.species
        new.level = self.level
        new.attack = self.attack
        new.spAttack = self.spAttack
        new.currentHP = self.currentHP
        new.maxHP = self.maxHP
        new.defense = self.defense
        new.spDef = self.spDef
        new.speed = self.speed
        return new

    #Function to add level up stats to a cellmon
    def level_up(self):
        self.maxHP = self.maxHP + self.baseHP
        self.attack = self.attack + self.baseAttack
        self.spAttack = self.spAttack + self.baseSpAttack
        self.defense = self.defense + self.baseDefense
        self.spDef = self.spDef + self.baseSpDef
        self.speed = self.speed + self.baseSpeed
        self.level += 1

    #Function to print the stats of a cellmon
    def printMaxStats(self):
        response = []
        response.append(f"Species: {self.species}\nLevel: {self.level}\nMaximum HP: {self.maxHP}\nCurrent HP: {self.currentHP}\nAttack: {self.attack}\nDefense: {self.defense}\nSpAttack: {self.spAttack}\nSpDef: {self.spDef}\nSpeed: {self.speed}")
        return response

    #Function to calculate physical damage
    def doPhysAttack(self, user):
        response = []
        damage = self.attack + random.randint(-2,2)
        if user.party[0] == self:
            name = f"{user.name}'s"
        else:
            name = "Enemy"
        response.append(f"{name} {self.species} attacked for {damage} damage!")
        return damage, response

    #Function to calculate special damage
    def doSpecialAttack(self, user):
        response = []
        damage = self.spAttack + random.randint(-2,2)
        if user.party[0] == self:
            name = f"{user.name}'s"
        else:
            name = "Enemy"
        response.append(f"{name} {self.species} attacked for {damage} damage!")
        return damage, response

    #Function to apply physical damage
    def takePhysDamage(self, user, damage):
        global win, lose
        response = []
        damageCalc = (int)(self.defense * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)

        if user.party[0] == self:
            name = f"{user.name}'s"
        else:
            name = "Enemy"

        if self.currentHP > 0:
            response.append(f"{name} {self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")
        elif name == "Enemy":
            response.append(f"{name} {self.species} has been eaten!")
            win, lose = True, False
        elif user.party[0] == self:
            response.append(f"{name} {self.species} has been eaten!")
            user.party.remove(user.party[0])
            if len(user.party) > 0:
                response.append(f"{user.name} sent out {user.party[0].species}!")
                win, lose = False, False
            else:
                response.append(f"\n{user.name} has been eaten!")
                win, lose = False, True

        return response, win, lose

    #Function to apply special damage
    def takeSpecDamage(self, user, damage):
        global win, lose
        response = []
        damageCalc = (int)(self.spDef * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)

        if user.party[0] == self:
            name = f"{user.name}'s"
        else:
            name = "Enemy"

        if self.currentHP > 0:
            response.append(f"{name} {self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")
        elif name == "Enemy":
            response.append(f"{name} {self.species} has been eaten!")
            win, lose = True, False
        elif user.party[0] == self:
            response.append(f"{name} {self.species} has been eaten!")
            user.party.remove(user.party[0])
            if len(user.party) > 0:
                response.append(f"{user.name} sent out {user.party[0].species}!")
                win, lose = False, False
            else:
                response.append(f"\n{user.name} has been eaten!")
                win, lose = False, True

        return response, win, lose

############################################ Unique cellmon classes ##############################################
class aichu(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=3, baseSpAttack=3, baseDefense=3, baseSpDef=3, baseSpeed=3,
                 starterHP=2, starterAttack=2, starterSpAttack=2, starterDef=2, starterSpDef=2, starterSpeed=2,
                 species="Aichu"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class terrasaur(Cellmon):
    def __init__(self, level, baseHP=4, baseAttack=2, baseSpAttack=3, baseDefense=5, baseSpDef=6, baseSpeed=2,
                 starterHP=4, starterAttack=2, starterSpAttack=2, starterDef=2, starterSpDef=6, starterSpeed=4,
                 species="Terrasaur"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class verizard(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=2, baseDefense=3, baseSpDef=2, baseSpeed=4,
                 starterHP=1, starterAttack=2, starterSpAttack=2, starterDef=2, starterSpDef=3, starterSpeed=4,
                 species="Verizard"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class gekkip(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=5, baseDefense=2, baseSpDef=3, baseSpeed=2,
                 starterHP=1, starterAttack=3, starterSpAttack=2, starterDef=4, starterSpDef=2, starterSpeed=1,
                 species="Gekkip"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class capybrawla(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=1, baseSpAttack=2, baseDefense=5, baseSpDef=3, baseSpeed=1,
                 starterHP=3, starterAttack=4, starterSpAttack=3, starterDef=1, starterSpDef=2, starterSpeed=4,
                 species="Capybrawla"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class beesiege(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=1, baseSpAttack=2, baseDefense=5, baseSpDef=3, baseSpeed=1,
                 starterHP=3, starterAttack=4, starterSpAttack=3, starterDef=1, starterSpDef=2, starterSpeed=4,
                 species="Beesiege"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class jellyfists(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Jellyfists"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class doomosaur(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Doomsaur"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class parsnipe(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Parsnipe"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class pandamonium(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Pandamonium"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class fiamelon(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Fiamelon"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class armordillo(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Armordillo"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class jarceus(Cellmon):
    def __init__(self, level, baseHP=5, baseAttack=3, baseSpAttack=4, baseDefense=3, baseSpDef=4, baseSpeed=3,
                 starterHP=2, starterAttack=6, starterSpAttack=3, starterDef=3, starterSpDef=2, starterSpeed=6,
                 species="Jarceus"):
        self.maxHP = starterHP + (baseHP * level)
        self.attack = starterAttack + (baseAttack * level)
        self.spAttack = starterSpAttack + (baseSpAttack * level)
        self.defense = starterDef + (baseDefense * level)
        self.spDef = starterSpDef + (baseSpDef * level)
        self.speed = starterSpeed + (baseSpeed * level)
        self.species = species
        self.level = level

        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

#Location class creates an area for user to explore and defines enemy mobs
class Location:
    def __init__(self, Aname, mobs):
        self.Aname = Aname
        self.mobs = mobs[:4]

    #Function to encounter a random mob in each area
    def encounter(self):
        for x in range(1):
            randNum = random.randrange(1, 101)
            if 1 <= randNum <= 30:
                return self.mobs[0]
            elif 31 <= randNum <= 60:
                return self.mobs[1]
            elif 61 <= randNum <= 90:
                return self.mobs[2]
            else:
                return self.mobs[3]

#Creating the starter cellmon
Starter1=terrasaur(3)
Starter2=jellyfists(3)
Starter3=fiamelon(3)

#Creating the enemy mobs
A1=aichu(1)
A2=terrasaur(2)
A3=verizard(3)
A4=gekkip(4)
A5=capybrawla(5)
A6=beesiege(6)
A7=jellyfists(7)
A8=doomosaur(8)
A9=parsnipe(9)
A10=pandamonium(10)
A11=fiamelon(11)
A12=armordillo(12)
A13=jarceus(13)

#Creating the areas to explore
L1=Location("Fields",[A1,A2,A3,A13])
L2=Location("Mountains",[A4,A5,A6,A13])
L3=Location("Forest",[A7,A8,A9,A13])
L4=Location("Lake",[A10,A11,A12,A13])

#Function for user to search locations
def Cellsearch(user, msg_input):
    #global Game

    output = []

    if msg_input == "fields": #Searching fields
        found = L1.encounter()
    elif msg_input == "mountains": #Searching mountains
        found = L2.encounter()
    elif msg_input == "forest": #Searching Forest
        found = L3.encounter()
    elif msg_input == "lake": #Searching Lake
        found = L4.encounter()

    output.append(f"{user.name} has encountered a {found.species}!")

    return output, found

#Function to print user's cellmon party
def playerparty(user):
    party = True;
    num, i = 1, 0
    output = []

    #Print the cellmon
    while i < len(user.party):
        output.append(f"\n{num}. {user.party[i].species} <level {user.party[i].level}>")
        num = num + 1
        i = i + 1

    return output

#This function will check the speed of both player and mob, then result is sent back
def checkSpeed(player_mon, mob):
    if player_mon.speed > mob.speed: #Player is faster
        return 1
    elif player_mon.speed == mob.speed: #Equal speed, randomize
        return random.randint(0, 1)
    else: #Enemy is faster
        return 0

#This function will calculate damage for the attacks
def attackMob(player, mob, speed_, choice):
    response1 = []
    response2 = []
    global win, lose

    print(f"CURRENT SPEED ----> {speed_}")

    if choice == "attack": #Regular Attack
        if speed_ == 1: #Player attacks first
            damage, response1 = player.party[0].doPhysAttack(player)
            response2, win, lose = mob.takePhysDamage(player, damage)
        else: #Enemy attacks first
            damage, response1 = mob.doPhysAttack(player)
            response2, win, lose = player.party[0].takePhysDamage(player, damage)
    elif choice == "spAttack": #Special Attack
        if speed_ == 1: #Player attacks first
            damage, response1 = player.party[0].doSpecialAttack(player)
            response2, win, lose = mob.takeSpecDamage(player, damage)
        else: #Enemy attacks first
            damage, response1 = mob.doSpecialAttack(player)
            response2, win, lose = player.party[0].takeSpecDamage(player, damage)

    response1.extend(response2)
    return response1, win, lose

#This function will display a message whether or not the mob is successfully caught
def captureMob(player, mob):
    global win
    response = []
    caught = 0

    if mob.currentHP <= mob.maxHP * 0.5:
        win = True #mob caught, set condition
    else:
        caught = random.randint(0, 10)

        if caught >= 5:
            win = True #mob not caught
        else:
            win = False #mob not caught

    if win is True: #Caught
        if len(player.party) < 3: #Check if player's party is full
            response.append(f"{mob.species} was successfully caught!")
            mob.currentHP = mob.maxHP
            mob = mob.Cellcapture() #Create a new copy of the mob
            player.party.append(mob) #Add the mob to the party
        else:
            response.append(f"{mob.species} was successfully caught, but {player.name}'s party is full!")
    else: #Failed to catch
        response.append(f"Failed to capture {mob.species}!")
    return response, win #Returns a condition for ending the battle or not

#This function will display a message whether or not the battle is fled
def fleeBattle(player):
    chance = random.randint(0, 100)
    response = []
    global flee

    if chance <= 75:
        flee = True #Player fled, set condition
    else:
        flee = False #Player failed to flee

    if flee is True: #Player fled
        response.append(f"{player.name} fleed the battle.")
    else: #Player could not flee
        response.append(f"{player.name} could not flee.")
    return response, flee #Returns a condition for ending the battle or not
