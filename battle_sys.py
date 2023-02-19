from gameclass import *
import random

#Function to initiate a mob battle, gives user multiple options for the battle
def initiateBattle(player, mob):
    print(f"{player.name} has encountered a {mob.species}!")

    win_cnd, flee_cnd = False, False #Loop conditions
    
    player_mon = checkCnd(player) #Get current battle cellmon from user's party
    print(f"{player.name} sent out {player_mon.species}!")

    #Loop until user successfully flees the battle
    while win_cnd is False and flee_cnd is False:
        choice = getChoice() #Recursively get user input

        speed_ = checkSpeed(player_mon, mob) #Check to see if user or mob is faster        
        hp_ = 2

        #Attack choices
        if choice == "1" or choice == "2":
            if choice == "1": #Regular attack
                attackMob(player_mon, mob, speed_)
            elif choice == "2": #Special attack
                specialAtkMob(player_mon, mob, speed_)            
            hp_ = checkHP(player_mon, mob)
            if hp_== 0: #Player's current mon has fainted
                player_mon = checkCnd(player)
                if player_mon is None: #All player mons have fainted
                    print(f"{player.name} has no more usable cellmon. {player.name} has been eaten!")
                    break
            elif hp_ == 1: #Enemy mob has fainted
                win_cnd = True
        #Capture choice, if caught then exit battle
        elif choice == "3" or choice == "Capture":
            if mob.maxHP <= mob.baseHP * 0.5:
                captureMob(mob, True)
                win_cnd = True
            else:
                captureMob(mob, False)
        #Flee battle choice, calculates based on a random chance
        elif choice == "4" or choice == "Flee":
            chance = random.randint(0, 100)
            if chance >= 50:
                fleeBattle(player, True)
                flee_cnd = True
            else:
                fleeBattle(player, False)
    
    if win_cnd is True:
        winBattle(player)

#This function will check user input until a valid option is entered
def getChoice():
    choice = input("What would you like to do? Enter a number only.\n1. Attack\n2. Special Attack\n3. Capture\n4. Flee\n")
    if choice in ("1", "2", "3", "4"):
        return choice
    else:
        print("Please enter a valid option.")
        return getChoice()

#This function will check the conditions of the player's party cellmon
def checkCnd(player):
    if player.party[0].maxHP > 0:
        return player.party[0]
    elif player.party[1].maxHP > 0:
        return player.party[1]
    elif player.party[2].maxHP > 0:
        return player.party[2]
    else:
        return None

#This function will check the speed of both player and mob, then result is sent back
def checkSpeed(player_mon, mob):
    if player_mon.speed > mob.speed:
        speed_ = 1
    elif player_mon.speed == mob.speed:
        speed_ = random.randint(0, 1)
    else:
        speed_ = 0
    return speed_

#This function will check if the battle must end due to low HP
def checkHP(player_mon, mob):
    if player_mon.maxHP < 0:
        print(f"{player_mon.species} has fainted.")
        return 0
    elif mob.maxHP < 0:
        print(f"{mob.species} has fainted.")
        return 1
    else:
        print(f"{player_mon.species} has {player_mon.maxHP}hp left.")
        print(f"{mob.species} has {mob.maxHP}hp left.")        
        return 2

#Different messages to print during battle sequence
def printMsg(player_mon, mob, choice):
    if choice == 1:
        print(f"{player_mon.species} attacked {mob.species}!")
    elif choice == 2:
        print(f"{mob.species} attacked {player_mon.species}!")

#This function will calculate damage for a regular attack
def attackMob(player_mon, mob, speed_):
    if speed_ == 1:
        mob.maxHP = mob.maxHP - (player_mon.attack / mob.defense)
        printMsg(player_mon, mob, 1)
    else:
        player_mon.maxHP = player_mon.maxHP - (mob.attack / player_mon.defense)
        printMsg(player_mon, mob, 2)

def specialAtkMob(player_mon, mob, speed_):
    if speed_ == 1:
        mob.maxHP = mob.maxHP - (player_mon.spAttack / mob.spDef)
        printMsg(player_mon, mob, 1)
    else:
        player_mon.maxHP = player_mon.maxHP - (mob.spAttack / player_mon.spDef)
        printMsg(player_mon, mob, 2)

#This function will display a message whether or not the mob is successfully caught
def captureMob(mob, result):
    if result is True:
        print(f"{mob.species} was successfully caught!")
    else:
        print(f"Failed to capture {mob.species}!")

def winBattle(player):
    print(f"{player.name} has won the battle!\nLooks like your cellmon have gained some levels!")
    for mon in player.party:
        mon.level_up()

#This function will display a message whether or not the battle is fled
def fleeBattle(player, result):
    if result is True:
        print(f"{player.name} fleed the battle.")
    else:
        print(f"{player.name} could not flee.")

if __name__ == "__main__":
    party = [Aichu(1), Terrasaur(1), Verizard(1)]
    player = Player("Tucker", 1, party)
    mob = Gekkip(1)
    initiateBattle(player, mob)

