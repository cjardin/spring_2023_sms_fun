#Importing required libraries
import random
import json
import sys
sys.path.append('open_calls')
from twillio_webhook import *

from Main_Game_server import *
from battle_sys_server import *

mob = None
response = []
win = False
lose = False

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
        elif user.state == "getStarter":
            starter = msg_input.lower().Cellcapture()
            user.party.append(starter)
        elif user.state == "partyTime":
            output.append(GAME_LOGIC[ user.state ]['content'])
            output.append(playerParty())
        elif user.state == "display":
            num = int(msg_input)
            output.append(user.party[num].printMaxStats())
        elif user.state == "battle_init":
            response, user.currentEnemy = Cellsearch(msg_input.lower())
            output.append(response)
        elif user.state == "battle_start":
           output.append(f"{player.name} sent out {player.party[0].species}!")
        elif user.state == "attack" or user.state == "spAttack":
            speed = checkSpeed(user, user.currentEnemy)
            response, win, lose = attackMob(user, user.currentEnemy, speed, user.state))
            output.append(response)
        elif user.state == "stats":
            output.append(f"Printing stats:\n{player.name}'s Current Cellmon\n")
            output.append(user.party[0].printMaxStats())
            output.append("\nEnemy\n")
            output.append(user.currentEnemy.printMaxStats())
        elif user.state == "capture":
            response, win = captureMob(user, user.currentEnemy)
            output.append(response)
        elif user.state == "flee":
            response, win = fleeBattle(user)
            output.append(response)
        else:
            output.append(GAME_LOGIC[ user.state ]['content'])

        if win is True:
            output.append(f"{player.name} has won the battle!\nLooks like your cellmon have gained some levels!")
            for mon in player.party: #Loop through player's party and level up each cellmon
                if mon != user.currentEnemy: #Recently caught enemy mob will not be leveled up
                    mon.level_up()
                    mon.currentHP = mon.maxHP
                    output.append(mon.printMaxStats())
            user.state = "menu"
        elif lose is True:
            user.state = "end"
        else:
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
    def doPhysAttack(self):
        response = []
        damage = self.attack + random.randint(-2,2)
        response.append(f"{self.species} attacked for {damage} damage!")
        return damage, response

    #Function to calculate special damage
    def doSpecialAttack(self):
        response = []
        damage = self.spAttack + random.randint(-2,2)
        response.append(f"{self.species} attacked for {damage} damage!")
        return damage, response

    #Function to apply physical damage
    def takePhysDamage(self, user, damage):
        response = []
        damageCalc = (int)(self.defense * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)
        if self.currentHP > 0:
            response.append(f"{self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")
        else:
            response.append(f"{self.species} has been eaten!")
            user.party.remove(self.party[0])
            if user.party is not None:
                response.append(f"{user.name} sent out {self.party[0].species}!")
                win, lose = False, False
            else:
                response.append(f"\n{user.name} has been eaten!")
                win, lose = False, True

        return response, win, lose

    #Function to apply special damage
    def takeSpecDamage(self, damage):
        response = []
        damageCalc = (int)(self.spDef * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)
        if self.currentHP > 0:
            response.append(f"{self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")
        else:
            response.append(f"{self.species} has been eaten!")
            user.party.remove(self.party[0])
            if user.party is not None:
                response.append(f"{user.name} sent out {self.party[0].species}!")
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
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=2, baseSpeed=4,
                 starterHP=1, starterAttack=4, starterSpAttack=3, starterDef=2, starterSpDef=3, starterSpeed=4,
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
