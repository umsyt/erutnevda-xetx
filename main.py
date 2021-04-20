import random
code = random.randint(1000,9999)
solved = False
switc = False
woah = "retsym"

def parse(quer):
  inp = input(quer)
  act = inp.split(" ")
  return act

me = {"loc": "cr"}
exits = {"cr":{"d" : "dr", "w": "wr", "plugh":"xyzzy"},
        "dr":{"d" : "wr", "w": "cr"},
        "wr":{"d" : "cr", "w": "dr"},
        "dar":{"k" : "dr"},
        "dkr":{"a" : "dr"},
        "war":{"d" : "car", "w" : "dar"},
        "wkr":{"d" : "ckr", "w" : "dkr"},
        "car":{"d" : "dar", "w" : "war"},
        "ckr":{"d" : "dkr", "w" : "wkr"},
        "xyzzy":{"unplugh": "cr"}}
desc = {"cr":"A dark, seemingly dingy room. You can make out a screen.",
        "wr":"Also dark. There seems to be a switch which you can [toggle].",
        "dr":"A [keypad] and a device.",
        "dar":"Nothing but a scrap of [paper].",
        "dkr":"Another [keypad]? This one has a full keyboard.",
        "war":"You \033[94mb\033[0ma\033[91mr\033[92mg\033[0me in and see some slots you can [fill <object> <1/2/3>].",
        "car":"Mostly empty. Just a <blue-rock> which you can [take].",
        "wkr":"Mostly empty. Just a <red-rock> which you can [take].",
        "ckr":"Mostly empty. Just a <green-rock> which you can [take].",
        "xyzzy":"Welkom 2 da sekrett room!\nThere's not much doe. U can [unplugh] iff you want..."}
abrv = {"d": "[d]eosil",
        "w": "[w]iddershins",
        "a": "[a]na",
        "k": "[k]ata"}
objs = {
  "red-rock":"wkr",
  "green-rock":"ckr",
  "blue-rock":"car"
}
slots = {
  "1" : "",
  "2" : "",
  "3" : ""
}

print("""
BRAINDOWN: THE INTERACTIVE FRICTION
v.1.0.0 (technically all puzzles are implemented)
Welcome, dear traveler to-
to...
Honestly, I don't know where.
""")

name = input("What would you like to call yourself? ")

if name == "":
  name = "Unnamed Traveler"

print(f"""
Amazing.
Actions and objects are written in [brackets].
You can check your location with "whereami" and inventory with "inv".
You're on your own from here, {name}.
...
""")

tvtsr = False

while not solved and not tvtsr:
  #describe
  
  print(desc[me['loc']])
  
  if me['loc'] == "cr":
   if switc:
     print(f"It says \"{code}\".")
   else:
     print("It's off.")

  if me['loc'] == "wr":
   if switc:
     print(f"The switch is on.")
   else:
     print("The switch is off.")

  print()

  print("current exits:")
  for i in exits[me['loc']].keys():
    if i not in ["plugh", "unplugh"]:
      print(abrv[i])
  
  #ask
  act = parse("do?  ")
  print()
  
  
  # handle block
  def rp(a,p):
    global act, me
    return act[0] == a and me['loc'] == p

  if act[0] in "dawk" or act[0] == "plugh":
    me['loc'] = exits[me['loc']][act[0]]
  
  if act[0] in ["i", "inv", "inventory"]:
    for obj in objs.keys():
      if objs[obj] == "inv":
        print("-"+obj+"-")

  if act[0] in ["location", "where", "whereami"]:
    print(me['loc'])

  if rp("toggle","wr"):
    switc = not switc

  if rp("keypad","dr"):
    print("It awaits a [code <set of digits>].")
  
  if rp("code","dr"):
    if act[1] == str(code) or act[1] == "inri":
      print("The device whirrs...")
      exits["dr"]["a"] = "dar"
      exits["dr"]["k"] = "dkr"
      print("""           \033[1m
        ! You have activated the Tetramove Operation System !
You can now move in directions [a]na and [k]ata in TOS enabled rooms                            \033[0m""")
    else:
      print("The keypad gives a curt beep.")
  
  if rp("paper","dar"):
    print("""
    It reads:

    pain = "misery"
    fear = "death"
    love = "insanity"
    # Now hear my laboured breath...
    key = pain[0] + love[-1] + pain[2] + fear[-2] + pain[3:]
    #the key will let you out...

    Odd.
    """)

  if rp("keypad","dkr"):
    print("give me da [key <string>]!!! 🥺 ")
  
  if rp("key","dkr"):
    if act[1] == (woah[::-1] + chr(121)):
      print("You hear many doors shutter open.")
      exits["dar"]["w"] = "car"
      exits["dar"]["d"] = "war"
      exits["dkr"]["w"] = "ckr"
      exits["dkr"]["d"] = "wkr"
    else:
      print("bad key...")
  nune = "Mostly empty."

  if act[0] == "drop":
    if objs[act[1]] == "inv":
      objs[act[1]] = me["loc"]

  if act[0] == "take":
    if objs[act[1]] == me["loc"]:
      objs[act[1]] = "inv"
    for i in slots:
      if slots[i] == act[1]:
        slots[i] = ""
  
  if rp("fill", "war"):
    try:
      if objs[act[1]] == "inv" and slots[act[2]] == "": 
        objs[act[1]] = "war"
        slots[act[2]] = act[1] 
    except:
      print("oh dear, that didn't work...")

  if act[0] == "what-a-slot":
    print(slots)

  if slots == {'1': 'blue-rock', '2': 'red-rock', '3': 'green-rock'}:
    print("The room trembles as the energies align...")
    print()
    solved = True

  if me["loc"] == "cr":
    hm = random.randint(1,10)
    if hm == 7:
      print("A hullow voice says [plugh]...")

  if rp("unplugh", "xyzzy"):
    me["loc"] = "cr"

  if act[0] == "letmeoutp":
    solved = True


print("""
You have escaped the strange area!
Live the rest of your wonderful life! At least for now...

demo over. come back for better mechanics, secret rooms, and a story maybe.""")
