class Player:
    def __init__(user, name, number, party):
        user.name = name
        user.number = number
        user.party = party[:3]


class Cellmon:

    def __init__(self, level, baseAttack=0, baseDefense=0, baseSpDef=0, baseSpeed=0, baseHP=0, baseSpAttack=0, species ="Cellmon"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.speed = baseSpeed * level
        self.spDef = baseSpDef * level
        self.defense = baseDefense * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level

        self.baseHP = baseHP
        self.currentHP = baseHP
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpeed = baseSpeed
        self.baseSpAttack = baseSpAttack
        self.baseSpDef = baseSpDef

    def level_up(self):
        print("You've leveled up! ")
        self.maxHP = self.maxHP + self.baseHP
        self.attack = self.attack + self.baseAttack
        self.defense = self.defense + self.baseDefense
        self.spAttack = self.spAttack + self.baseSpAttack
        self.spDef = self.spDef + self.baseSpDef
        self.speed = self.speed + self.baseSpeed
        self.level += 1
        self.printMaxStats()

    def printMaxStats(self):
        print("Species: ",self.species, "\nLevel: ", self.level, "\nMaximum HP: ", self.maxHP, "\nAttack: ", self.attack, "\nDefense: ",
              self.defense, "\nSpAttack: ", self.spAttack)
        print("SpDef: ", self.spDef, "\nSpeed: ", self.speed)


class Aichu(Cellmon):
    def __init__(self, level, baseAttack=4, baseDefense=2, baseSpDef=3, baseSpeed=5, baseHP=10, baseSpAttack=12, species = "Aichu"):
        self.species = species
        self.level = level
        self.maxHP = baseHP * level
        self.speed = baseSpeed * level
        self.spDef = baseSpDef * level
        self.defense = baseDefense * level
        self.attack = baseAttack * level
        self.spAttack = baseSpAttack * level
        self.baseHP = baseHP
        self.currentHP = baseHP
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpeed = baseSpeed
        self.baseSpAttack = baseSpAttack
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
