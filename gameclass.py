#Importing required libraries
import random

#Defines the user's class for the game (name, phone #, and cellmon party)
class Player:
    def __init__(user, name, number, party):
        user.name = name
        user.number = number
        user.party = party[:2]

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
        print("You've leveled up! ")
        self.maxHP = self.maxHP + self.baseHP
        self.attack = self.attack + self.baseAttack
        self.spAttack = self.spAttack + self.baseSpAttack
        self.defense = self.defense + self.baseDefense
        self.spDef = self.spDef + self.baseSpDef
        self.speed = self.speed + self.baseSpeed
        self.level += 1
        self.printMaxStats()

    #Function to print the stats of a cellmon
    def printMaxStats(self):
        print("Species: ", self.species, "\nLevel: ", self.level, "\nMaximum HP: ", self.maxHP, "\nCurrent HP: ",self.currentHP, "\nAttack: ",
              self.attack, "\nDefense: ",
              self.defense, "\nSpAttack: ", self.spAttack)
        print("SpDef: ", self.spDef, "\nSpeed: ", self.speed)

    #Function to calculate physical damage
    def doPhysAttack(self):
        damage = self.attack + random.randint(-1,1)
        print(f"{self.species} attacked for {damage} damage!")
        return damage

    #Function to calculate special damage
    def doSpecialAttack(self):
        damage = self.spAttack + random.randint(-1,1)
        print(f"{self.species} attacked for {damage} damage!")
        return damage

    #Function to apply physical damage
    def takePhysDamage(self, damage):
        damageCalc = (int)(self.defense * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)
        if self.currentHP > 0:
            print(f"{self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")

    #Function to apply special damage
    def takeSpecDamage(self, damage):
        damageCalc = (int)(self.spDef * .1 * damage)
        self.currentHP = (self.currentHP - damageCalc)
        if self.currentHP > 0:
            print(f"{self.species} took {damageCalc} damage! {self.species}'s current HP is {self.currentHP}")

############################################ Unique cellmon classes ##############################################
class Aichu(Cellmon):
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

class Terrasaur(Cellmon):
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

class Verizard(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=2, baseSpAttack=4, baseDefense=3, baseSpDef=2, baseSpeed=4,
                 starterHP=1, starterAttack=3, starterSpAttack=3, starterDef=2, starterSpDef=3, starterSpeed=4,
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

class Gekkip(Cellmon):
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

class Capybrawla(Cellmon):
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

class Beesiege(Cellmon):
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

class Jellyfists(Cellmon):
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

class Doomosaur(Cellmon):
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

class Parsnipe(Cellmon):
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

class Pandamonium(Cellmon):
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

class Fiamelon(Cellmon):
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

class Armordillo(Cellmon):
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

class Jarceus(Cellmon):
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
            if 1 <= randNum <= 31:
                return self.mobs[0]
            elif 32 <= randNum <= 62:
                return self.mobs[1]
            elif 63 <= randNum <= 93:
                return self.mobs[2]
            else:
                return self.mobs[3]

#Testing system
#pikablu = Aichu(2)
#pikablu.printMaxStats()
#pikablu.level_up()

#enemy = Doomosaur(2)
#enemy.printMaxStats()
#enemy.takePhysDamage(pikablu.doPhysAttack())
#enemy.printMaxStats()
