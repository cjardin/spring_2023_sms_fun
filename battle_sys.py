#Import required libraries
from gameclass import * #Base game info
import random

#Main Function to initiate a mob battle, gives user multiple options for the battle
def initiateBattle(player, mob):
    print(f"{player.name} has encountered a {mob.species}!")

    win_cnd, flee_cnd = False, False #Loop conditions
    
    player_mon = player.party[0] #Get current battle cellmon from user's party
    print(f"{player.name} sent out {player_mon.species}!")

    #Loop until user successfully wins, loses, or flees the battle
    while win_cnd is False and flee_cnd is False:
        choice = getChoice() #Recursively get user input
        print("")
        
        speed_ = checkSpeed(player_mon, mob) #Check to see if user or mob is faster        

        #Checking user input and executing required actions
        if choice == "1" or choice == "2": #Attack Choices
            attackMob(player_mon, mob, speed_, choice) #User or mob may attack
            win_cnd, remove_mon = checkHP(player, player_mon, mob) #Check for winning condition or lost cellmon
            if remove_mon is True: #Checking if player's mon was eaten
                player.party.remove(player_mon) #Remove the cellmon from the party
                player_mon = checkCnd(player) #Get next cellmon from party
        elif choice == "3": #Print stats of player and enemy mob
            print(f"Printing stats:\n{player.name}'s Current Cellmon")
            player_mon.printMaxStats()
            print("\nEnemy")
            mob.printMaxStats()
            print("")
        elif choice == "4": #Capture choice, if caught then exit battle
            if mob.maxHP <= mob.baseHP * 0.5:
                win_cnd = captureMob(player, mob, True) #mob caught, set condition
            else:
                win_cnd = captureMob(player, mob, False) #mob not caught
        elif choice == "5": #Flee battle choice, calculates based on a random chance
            chance = random.randint(0, 100)
            if chance >= 50:
                flee_cnd = fleeBattle(player, True) #Player fled, set condition
            else:
                flee_cnd = fleeBattle(player, False) #Player failed to flee
    
        #Checking if further action is needed
        if choice in ("4", "5") and (win_cnd is False and flee_cnd is False): #Checking if mob needs to attack after failed catch or flee
            choice = random.randint(1, 2)
            attackMob(player_mon, mob, 0, str(choice)) #Mob attacks randomly
            win_cnd, remove_mon = checkHP(player, player_mon, mob) #Check for winning condtion or lost cellmon
            if remove_mon is True: #Checking if player's mon was eaten
                player.party.remove(player_mon) #Remove the cellmon from the party
                player_mon = checkCnd(player) #Get next cellmon from party
        elif choice in ("1", "2") and win_cnd is False: #Checking if player or mob still need to attack
            if speed_ == 1:
                choice = random.randint(1, 2)
                attackMob(player_mon, mob, 0, str(choice)) #Mob attacks randomly
            else:
                attackMob(player_mon, mob, 1, choice) #Player attacks
            win_cnd, remove_mon = checkHP(player, player_mon, mob) #Check for winning condition or lost cellmon
            if remove_mon is True: #Checking if player's mon was eaten
                player.party.remove(player_mon) #Remove the cellmon from the party
                player_mon = checkCnd(player) #Get next cellmon from party       

        #Check if all player mons are eaten, then break out of loop if player died
        if player_mon is None:
            print(f"{player.name} has no more usable cellmon. {player.name} has been eaten!")
            break

        #Print health of both parties while battle is still ongoing
        if win_cnd is False and flee_cnd is False:
            print(f"{player_mon.species} has {player_mon.maxHP}hp left.")
            print(f"{mob.species} has {mob.maxHP}hp left.")

    #Check if user won or fled the battle
    if win_cnd is True: #Player won or caught the cellmon
        winBattle(player, mob) #Display winning message and stats
        return True
    elif flee_cnd is True: #Player fled
        return True
    else: #Player died
        return False

#This function will check if player's cellmon was eaten or enemy mob was defeated
#It returns a condition for continuing the battle
def checkHP(player, player_mon, mob):
    if player_mon.maxHP < 0: #Player's cellmon was eaten
        print(f"{player_mon.species} has been eaten!")
        return False, True #Battle must continue
    elif mob.maxHP < 0: #Enemy mob defeated
        print(f"{mob.species} has been eaten.")
        return True, False #Battle is won
    else: #Battle must continue
        return False, False

#This function will check user input until a valid option is entered
def getChoice():
    choice = input("\nWhat would you like to do? Enter a number only.\n1. Attack\n2. Special Attack\n3. Check Stats\n4. Capture\n5. Flee\n")
    if choice in ("1", "2", "3", "4", "5"):
        return choice
    else:
        print("Please enter a valid option.")
        return getChoice() #Recursively call function until correct input is given

#This function will check the conditions of the player's party cellmon
def checkCnd(player):
    for mon in player.party: #Check each cellmon in party
        if mon.maxHP > 0: #Current cellmon is fit for battle, return it
            print(f"{player.name} sent out {mon.species}!")
            return mon
    return None #All cellmon in party have been eaten, player is eaten

#This function will check the speed of both player and mob, then result is sent back
def checkSpeed(player_mon, mob):
    if player_mon.speed > mob.speed: #Player is faster
        return 1
    elif player_mon.speed == mob.speed: #Equal speed, randomize
        return random.randint(0, 1)
    else: #Enemy is faster
        return 0

#This function will calculate damage for the attacks
def attackMob(player_mon, mob, speed_, choice):
    if choice == "1": #Regular Attack
        if speed_ == 1: #Player attacks first
            mob.maxHP = mob.maxHP - (player_mon.attack / mob.defense)
            print(f"{player_mon.species} attacked {mob.species}!")
        else: #Enemy attacks first
            player_mon.maxHP = player_mon.maxHP - (mob.attack / player_mon.defense)
            print(f"{mob.species} attacked {player_mon.species}!")
    elif choice == "2": #Special Attack
        if speed_ == 1: #Player attacks first
            mob.maxHP = mob.maxHP - (player_mon.spAttack / mob.spDef)
            print(f"{player_mon.species} special attacked {mob.species}!")
        else: #Enemy attacks first
            player_mon.maxHP = player_mon.maxHP - (mob.spAttack / player_mon.spDef)
            print(f"{mob.species} special attacked {player_mon.species}!")

#This function will display a message whether or not the mob is successfully caught
def captureMob(player, mob, result):
    if result is True: #Caught
        print(f"{mob.species} was successfully caught!")
        player.party.append(mob)
    else: #Failed to catch
        print(f"Failed to capture {mob.species}!")
    return result #Returns a condition for ending the battle or not

#This function will display a win msg and level up the remaining cellmon
def winBattle(player, mob):
    print(f"{player.name} has won the battle!\nLooks like your cellmon have gained some levels!")
    for mon in player.party: #Loop through player's party and level up each cellmon
        if mon != mob: #Recently caught enemy mob will not be leveled up
            mon.level_up()

#This function will display a message whether or not the battle is fled
def fleeBattle(player, result):
    if result is True: #Player fled
        print(f"{player.name} fleed the battle.")
    else: #Player could not flee
        print(f"{player.name} could not flee.")
    return result #Returns a condition for ending the battle or not

#Testing system
party = [Aichu(1), Terrasaur(1), Verizard(1)] #Create a new party
player = Player("Tucker", 1, party) #Create a new player object
mob = Gekkip(1) #Create a new enemy mob
result = initiateBattle(player, mob) #Start the battle
if result is False: #If player was eaten print message
    print("Game Over")

