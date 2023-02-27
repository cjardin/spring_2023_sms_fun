#Import required libraries
from gameclass_server import * #Importing main game classes and functions
from battle_sys_server import *#Importing battle system

import sys
sys.path.append('open_calls')
from twillio_webhook import *

global Game #Create a global variable for game condition

NewUser=Player(" "," ",[]) #Create a new user object

#Creating the starter cellmon
Starter1=Terrasaur(2)
Starter2=Jellyfists(2)
Starter3=Fiamelon(2)

#Creating the enemy mobs
A1=Aichu(1)
A2=Terrasaur(2)
A3=Verizard(3)
A4=Gekkip(4)
A5=Capybrawla(5)
A6=Beesiege(6)
A7=Jellyfists(7)
A8=Doomosaur(8)
A9=Parsnipe(9)
A10=Pandamonium(10)
A11=Fiamelon(11)
A12=Armordillo(12)
A13=Jarceus(13)

#Creating the areas to explore
L1=Location("Fields",[A1,A2,A3,A13])
L2=Location("Mountains",[A4,A5,A6,A13])
L3=Location("Forest",[A7,A8,A9,A13])
L4=Location("Lake",[A10,A11,A12,A13])

#Function for user to search locations
def Cellsearch(user, msg_input):
    global Game

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
def playerparty():
    party = True;
    num, i = 1, 0
    output = []

    #Print the cellmon
    while i < len(NewUser.party):
        output.append(f"\n{num}. {NewUser.party[i].species} <level {NewUser.party[i].level}>")
        num = num + 1
        i = i + 1

    return output

#Start of game:
def start_game():
    #create_msg("New User detected. Please input your name.")
    test_text = str(request.form['Body'])
    NewUser.name = test_text

    #Print welcome info
    #create_msg(f"Welcome {NewUser.name}\nThis information isn't known to the public only users chosen can know the truth of these creatures.Cellmon...\nThese creatures are living across the cell living peacefully or fighting for territory. If they were to become violent and run rampant it could cause data corruption across.\nYour mission as a user is to capture or defeat as many of these creatures as possible.\nI will give you one to start with but be warned...If a Cellmon is defeated by another.\nTheir data becomes corrupt and disperses being absorbed by the victor.There is one that we warn all users to avoid at all cost. Jarceus...\nA Cellmon that has lived for years killing and absorbing any Cellmon it comes across.\nNow lets get your journey as a Cellmon trainer started.")

    starter=True

    #Get user input for choosing the starter cellmon
    while starter==True:
        #create_msg("Please Choose your Starter:\n1.Terrasaur\n2.Jellyfists\n3.Fiamelon\n")
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
            #create_msg("Invalid Cellmon Choice")

    #create_msg("Be careful... may you and your Cellmon stand above all")

    #User enters the danger zone
    Game = True

    #Loop while the user does not want to quit the game
    while Game== True:
        #create_msg("\n1.Search\n2.Party\n3.Quit")
        #create_msg("Choose an Action type out the action or number: ")
        test_text = str(request.form['Body'])
        test_input = test_text

        if test_input=="1" or test_input=="Search" or test_input=="search": #User chooses to search
            Cellsearch()
        elif test_input=="2" or test_input=="Party" or test_input=="party": #User chooses to see party
            playerparty()
        elif test_input=="3" or test_input=="Quit" or test_input=="quit": #User chooses to quit the game
            #create_msg("Thank you for playing")
            Game= False
        else:
            #create_msg("Invalid command please select an action")
