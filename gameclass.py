class Player:
    def __init__(user, name, number, party):
        user.name = name
        user.number = number
        user.party = party[:3]


class Cellmon:
#test commit on desktop installation
#test commit to personal branch, i will then push it on to the main brancch
    def __init__(self, level, baseHP=0, baseAttack=0, baseSpAttack=0, baseDefense=0, baseSpDef=0, baseSpeed=0, species ="Cellmon"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

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

    def printMaxStats(self):
        print("Species: ",self.species, "\nLevel: ", self.level, "\nMaximum HP: ", self.maxHP, "\nAttack: ", self.attack, "\nDefense: ",
              self.defense, "\nSpAttack: ", self.spAttack)
        print("SpDef: ", self.spDef, "\nSpeed: ", self.speed)


class Aichu(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Aichu"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Terrasaur(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Terrasaur"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Verizard(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Verizard"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Gekkip(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Gekkip"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Capybrawla(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Capybrawla"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Beesiege(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Beesiege"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Jellyfists(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Jellyfists"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Doomosaur(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Doomosaur"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Parsnipe(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Doomosaur"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

class Pandamonium(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Pandamonium"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef

class Fiamelon(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Fiamelon"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef
class Armordillo(Cellmon):
    def __init__(self, level, baseHP=3, baseAttack=4, baseSpAttack=5, baseDefense=2, baseSpDef=6, baseSpeed=4, species = "Armordillo"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.defense = baseDefense * level
        self.spDef = baseSpDef * level
        self.speed = baseSpeed * level


        self.baseHP = baseHP
        self.currentHP = self.maxHP
        self.baseAttack = baseAttack
        self.baseSpAttack = baseSpAttack
        self.baseDefense = baseDefense
        self.baseSpDef = baseSpDef

class Location:
    def __init__(Area, Aname, mobs):
        Area.Aname = Aname
        Area.mobs = mobs[:4]


cellmon = Cellmon(1)
cellmon.printMaxStats()
cellmon.level_up()

pikablu = Aichu(1)
pikablu.printMaxStats()
pikablu.level_up()
