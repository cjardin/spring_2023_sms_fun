class Player:
  def __init__(user, name, number, party):
    user.name = name
    user.number = number
    user.party = party[:3]


class Cellmon:
    def __init__(Cmon,Cname, HP,  Atck, SpAtck, Def, SpDef, Speed, Exp, level):
        Cmon.Cname= Cname
        Cmon.HP = HP
        Cmon.Atck = Atck
        Cmon.SpAtck = SpAtck
        Cmon.Def= Def
        Cmon.SpDef = SpDef
        Cmon.Speed = Speed
        Cmon.Exp= Exp
        Cmon.level= level

class Location:
    def __init__(Area, Aname, mobs):
        Area.Aname= Aname
        Area.mobs= mobs[:4]

def Cellmon_info(C):
    print("Name: "+ C.Cname )
    print("Level: "+ str(C.level))
    print("HP: "+ str(C.HP))
    print("Attack: "+ str(C.Atck))
    print("Defense: "+ str(C.Def))
    print("Special Attack: "+ str(C.SpAtck))
    print("Special Defense: "+ str(C.SpDef))
    print("Speed: "+ str(C.Speed))
    print("Exp: "+ str(C.Exp))
    
C1 = Cellmon("Aichu", 10, 3, 6, 2, 3, 5,0,1)
C2 = Cellmon("Terrasaur",12,7,2,4,2,4,0,1)
C3= Cellmon("Verizard",10,4,5,5,5,7,0,1)
C4= Cellmon("Gekkip",9,6,7,3,3,5,0,1)

L1= Location("Lake", [C2,C3,C4])

p1 = Player("Elijah","8585278481", [C1] )

print(p1.name)
print(p1.number)
Cellmon_info(p1.party[0])
C4.level= C4.level+1
print(C4.level)
for i in range(0, len(L1.mobs)):
    print(L1.mobs[i].Cname)



