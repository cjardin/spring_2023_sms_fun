
def Cellsearch():
 searching=True
 print("Please Choose a location to explore")
 print("1.Fields\n2.Mountains\n3.Forest\n4.Lake\n")
 while searching==True:
  search = input ()

  find = str(search)

  if find=="1" or find=="Fields" or find=="fields":
    print("searching the fields")
    searching=False
  elif find=="2" or find=="Mountains" or find=="mountains":
    print("searching the mountains")
    searching=False
  elif find=="3" or find=="Forest" or find=="forest":
    print("searching the forest")
    searching=False
  elif find=="4" or find=="Lake" or find=="lake":
    print("searching the forest")
    searching=False
    print("Displaying Cellmon Party")
  elif test_input=="3" or test_input=="Quit" or test_input=="quit":
    print("Thank you for playing")
    Game= False
  else:
    print("you walked around in a circle from walking aimlessly\n")
    print("Please Choose a location to explore")
    print("1.Fields\n2.Mountains\n3.Forest\n4.Lake\n")

Game = True
while Game== True:
 print ("1.Search\n2.Party\n3.Quit")
 test_text = input ("Choose an Action type out the action or number: ")

 test_input = str(test_text)

 if test_input=="1" or test_input=="Search" or test_input=="search":
    Cellsearch()
 else:
  print("Invalid command please select an action")
