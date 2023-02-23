class Player:
    def __init__(user, name, number, party, partynum):
        user.name = name
        user.number = number
        user.party = party[:3]
        user.partynum = partynum


class Cellmon:
    # test commit on desktop installation
    # please dear god work
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
        print("Species: ", self.species, "\nLevel: ", self.level, "\nMaximum HP: ", self.maxHP, "\nAttack: ",
              self.attack, "\nDefense: ",
              self.defense, "\nSpAttack: ", self.spAttack)
        print("SpDef: ", self.spDef, "\nSpeed: ", self.speed)

    def doPhysAttack(self):
        damage = self.attack
        print(self.species, " attacked for ", damage , " damage!")
        ID = 0
        return damage


    def doSpecialAttack(self):
        damage = self.SpecialAttack()
        ID = 1
        return damage

    def takePhysDamage(self, damage):
        damageCalc = (int)(self.defense*.100 * damage)
        self.currentHP = (self.currentHP - damageCalc)
        print(self.species, "took ", damageCalc, "damage!", self.species, "'s current HP is " , self.currentHP)

    def printCurrentHP(self):
        print(self.currentHP)

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


class Location:
    def __init__(Area, Aname, mobs):
        Area.Aname = Aname
        Area.mobs = mobs[:4]



pikablu = Aichu(2)
pikablu.printMaxStats()


enemy = Doomosaur(2)
enemy.printMaxStats()
enemy.takePhysDamage(pikablu.doPhysAttack())

