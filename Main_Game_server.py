#Import required libraries
import gameclass_server #Importing main game classes and functions
import battle_sys_server #Importing battle system

import sys
sys.path.append('open_calls')
from twillio_webhook import *

global Game #Create a global variable for game condition

NewUser=gameclass.Player(" "," ",[]) #Create a new user object

#Creating the starter cellmon
Starter1=gameclass.Terrasaur(2)
Starter2=gameclass.Jellyfists(2)
Starter3=gameclass.Fiamelon(2)

#Creating the enemy mobs
A1=gameclass.Aichu(1)
A2=gameclass.Terrasaur(2)
A3=gameclass.Verizard(3)
A4=gameclass.Gekkip(4)
A5=gameclass.Capybrawla(5)
A6=gameclass.Beesiege(6)
A7=gameclass.Jellyfists(7)
A8=gameclass.Doomosaur(8)
A9=gameclass.Parsnipe(9)
A10=gameclass.Pandamonium(10)
A11=gameclass.Fiamelon(11)
A12=gameclass.Armordillo(12)
A13=gameclass.Jarceus(13)

#Creating the areas to explore
L1=gameclass.Location("Fields",[A1,A2,A3,A13])
L2=gameclass.Location("Mountains",[A4,A5,A6,A13])
L3=gameclass.Location("Forest",[A7,A8,A9,A13])
L4=gameclass.Location("Lake",[A10,A11,A12,A13])

#Function for user to search locations
def Cellsearch():
    global Game
    
    searching=True

    create_msg("Please Choose a server to explore\n1. Fields Threat Level Max: 3\n2. Mountains Threat Level Max: 6\n3. Forest Threat Level Max: 9\n4. Lake Threat level Max: 12")

    while searching==True:
        search = str(request.form['Body'])

        find = search

    if find=="1" or find=="Fields" or find=="fields": #Searching fields
        found=L1.encounter()
        Game = battle_sys.initiateBattle(NewUser, found)
        searching=False
    elif find=="2" or find=="Mountains" or find=="mountains": #Searching mountains
        found=L2.encounter()
        Game = battle_sys.initiateBattle(NewUser, found)
        searching=False
    elif find=="3" or find=="Forest" or find=="forest": #Searching Forest
        found=L3.encounter()
        Game = battle_sys.initiateBattle(NewUser, found)
        searching=False
   elif find=="4" or find=="Lake" or find=="lake": #Searching Lake
        found=L4.encounter()
        Game = battle_sys.initiateBattle(NewUser, found)
        searching=False
    else:
        create_msg("you traveled around in a circle from invalid server choice\nPlease Choose a location to explore\n1.Fields\n2.Mountains\n3.Forest\n4.Lake\n")

#Function to print user's cellmon party
def playerparty():
    party = True;
    num, i = 1, 0

    #Print the cellmon
    while i < len(NewUser.party):
        create_msg(f"{num}. {NewUser.party[i].species} <level {NewUser.party[i].level}>")
        num = num + 1
        i = i + 1

    #Get user input for info
    while party== True:
        create_msg("Enter the # or name of the Cellmon in the party you want info on: ")
        test_text = str(request.form['Body'])
        test_input = test_text
        if test_input=="1" or test_input==NewUser.party[0].species:
            NewUser.party[0].printMaxStats()
        elif test_input=="2" or test_input==NewUser.party[1].species:
            NewUser.party[1].printMaxStats()
        elif test_input=="3" or test_input==NewUser.party[2].species:
            NewUser.party[2].printMaxStats()
        else:
            create_msg("Invalid Cellmon ID")
        party= False

#Start of game:
def start_game():
    create_msg("New User detected. Please input your name.")
    test_text = str(request.form['Body'])
    NewUser.name = test_text

    #Print welcome info
    create_msg(f"Welcome {NewUser.name}\nThis information isn't known to the public only users chosen can know the truth of these creatures.Cellmon...\nThese creatures are living across the cell living peacefully or fighting for territory. If they were to become violent and run rampant it could cause data corruption across.\nYour mission as a user is to capture or defeat as many of these creatures as possible.\nI will give you one to start with but be warned...If a Cellmon is defeated by another.\nTheir data becomes corrupt and disperses being absorbed by the victor.There is one that we warn all users to avoid at all cost. Jarceus...\nA Cellmon that has lived for years killing and absorbing any Cellmon it comes across.\nNow lets get your journey as a Cellmon trainer started.")

    starter=True

    #Get user input for choosing the starter cellmon
    while starter==True:
        create_msg("Please Choose your Starter:\n1.Terrasaur\n2.Jellyfists\n3.Fiamelon\n")
        test_txt = str(request.form['Body'])
        Starterpick = test_text

        #User chooses a starter
        if Starterpick=="1" or Starterpick=="Terrasaur" or Starterpick=="terrasaur":
            NewUser.party.append(Starter1)
            starter=False
        elif Starterpick=="2" or Starterpick=="Jellyfists" or Starterpick=="jellyfists":
            NewUser.party.append(Starter2)
            starter=False
        elif Starterpick=="3" or Starterpick=="Fiamelon" or Starterpick=="fiamelon":
            NewUser.party.append(Starter3)
            starter=False
        else:
            create_msg("Invalid Cellmon Choice")

    create_msg("Be careful... may you and your Cellmon stand above all")

    #User enters the danger zone
    Game = True

    #Loop while the user does not want to quit the game
    while Game== True:
        create_msg("\n1.Search\n2.Party\n3.Quit")
        create_msg("Choose an Action type out the action or number: ")
        test_text = str(request.form['Body'])
        test_input = test_text

        if test_input=="1" or test_input=="Search" or test_input=="search": #User chooses to search
            Cellsearch()
        elif test_input=="2" or test_input=="Party" or test_input=="party": #User chooses to see party
            playerparty()
        elif test_input=="3" or test_input=="Quit" or test_input=="quit": #User chooses to quit the game
            create_msg("Thank you for playing")
            Game= False
        else:
            create_msg("Invalid command please select an action")
