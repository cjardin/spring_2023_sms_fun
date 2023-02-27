#Import required libraries
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
        
        speed_ = checkSpeed(player_mon, mob) #Check to see if user or mob is faster        

        #Checking user input and executing required actions
        if choice == "1" or choice == "2": #Attack Choices
            attackMob(player_mon, mob, speed_, choice) #User or mob may attack
            win_cnd, player_mon, dead = checkHP(player, player_mon, mob) #Check for winning condition or lost cellmon
        elif choice == "3": #Print stats of player and enemy mob
            print(f"Printing stats:\n{player.name}'s Current Cellmon")
            player_mon.printMaxStats()
            print("\nEnemy")
            mob.printMaxStats()
            print("")
        elif choice == "4": #Capture choice, if caught then exit battle
            if mob.currentHP <= mob.maxHP * 0.5:
                win_cnd, mob = captureMob(player, mob, True) #mob caught, set condition
            else:
                caught = random.randint(0, 10)
                if caught >= 5:
                    win_cnd, mob = captureMob(player, mob, True) #mob not caught
                else:
                    win_cnd, mob = captureMob(player, mob, False) #mob not caught
        elif choice == "5": #Flee battle choice, calculates based on a random chance
            chance = random.randint(0, 100)
            if chance <= 75:
                flee_cnd = fleeBattle(player, True) #Player fled, set condition
            else:
                flee_cnd = fleeBattle(player, False) #Player failed to flee
    
        #Checking if further action is needed
        if choice in ("4", "5") and (win_cnd is False and flee_cnd is False): #Checking if mob needs to attack after failed catch or flee
            choice = random.randint(1, 2)
            attackMob(player_mon, mob, 0, str(choice)) #Mob attacks randomly
            win_cnd, player_mon, dead = checkHP(player, player_mon, mob) #Check for winning condtion or lost cellmon
        elif choice in ("1", "2") and win_cnd is False: #Checking if player or mob still need to attack
            if speed_ == 1:
                choice = random.randint(1, 2)
                attackMob(player_mon, mob, 0, str(choice)) #Mob attacks randomly
                win_cnd, player_mon, dead = checkHP(player, player_mon, mob) #Check for winning condition or lost cellmon
            elif dead is False:
                attackMob(player_mon, mob, 1, choice) #Player attacks
                win_cnd, player_mon, dead = checkHP(player, player_mon, mob) #Check for winning condition or lost cellmon

        #Check if all player mons are eaten, then break out of loop if player died
        if player_mon is None:
            print(f"{player.name} has no more usable cellmon. {player.name} has been eaten!")
            print("Game Over. Thank you for playing Cellmon!")
            break

        #Print health of both parties while battle is still ongoing
        if win_cnd is False and flee_cnd is False:
            print(f"{player_mon.species} has {player_mon.currentHP}hp left.")
            print(f"{mob.species} has {mob.currentHP}hp left.")

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
    if player_mon.currentHP <= 0: #Player's cellmon was eaten
        print(f"{player_mon.species} has been eaten!")
        player.party.remove(player_mon) #Remove the cellmon from the party
        player_mon = checkCnd(player) #Get next cellmon from party
        return False, player_mon, True #Battle must continue
    elif mob.currentHP <= 0: #Enemy mob defeated
        print(f"{mob.species} has been eaten.")
        return True, player_mon, False #Battle is won
    else: #Battle must continue
        return False, player_mon, False

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
            damage = player_mon.doPhysAttack()
            mob.takePhysDamage(damage)
        else: #Enemy attacks first
            damage = mob.doPhysAttack()
            player_mon.takePhysDamage(damage)
    elif choice == "2": #Special Attack
        if speed_ == 1: #Player attacks first
            damage = player_mon.doSpecialAttack()
            mob.takeSpecDamage(damage)
        else: #Enemy attacks first
            damage = mob.doSpecialAttack()
            player_mon.takeSpecDamage(damage)

#This function will display a message whether or not the mob is successfully caught
def captureMob(player, mob, result):
    if result is True: #Caught
        if len(player.party) < 3: #Check if player's party is full
            print(f"{mob.species} was successfully caught!")
            mob.currentHP = mob.maxHP
            mob = mob.Cellcapture() #Create a new copy of the mob
            player.party.append(mob) #Add the mob to the party
        else:
            print(f"{mob.species} was successfully caught, but {player.name}'s party is full!")
    else: #Failed to catch
        print(f"Failed to capture {mob.species}!")
    return result, mob #Returns a condition for ending the battle or not

#This function will display a win msg and level up the remaining cellmon
def winBattle(player, mob):
    print(f"{player.name} has won the battle!\nLooks like your cellmon have gained some levels!")
    for mon in player.party: #Loop through player's party and level up each cellmon
        if mon != mob: #Recently caught enemy mob will not be leveled up
            mon.level_up()
            mon.currentHP = mon.maxHP

#This function will display a message whether or not the battle is fled
def fleeBattle(player, result):
    if result is True: #Player fled
        print(f"{player.name} fleed the battle.")
    else: #Player could not flee
        print(f"{player.name} could not flee.")
    return result #Returns a condition for ending the battle or not

