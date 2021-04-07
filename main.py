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
exits = {"cr":{"d" : "dr", "w": "wr"},
        "dr":{"d" : "wr", "w": "cr"},
        "wr":{"d" : "cr", "w": "dr"},
        "dar":{"k" : "dr"},
        "dkr":{"a" : "dr"}}
desc = {"cr":"A dark, seemingly dingy room. You can make out a screen.",
        "wr":"Also dark. There seems to be a switch which you can [toggle].",
        "dr":"A [keypad] and a device.",
        "dar":"Nothing but a scrap of [paper].",
        "dkr":"Another [keypad]? This one has a full keyboard."}
abrv = {"d": "[d]eosil",
        "w": "[w]iddershins",
        "a": "[a]na",
        "k": "[k]ata"}

print("""
BRAINDOWN: THE INTERACTIVE FRICTION
v.0.1.4 (2 puzzles!)
Welcome, dear traveler to-
to...
Honestly, I don't know where.
""")

name = input("What would you like to call yourself? ")

if name == "":
  name = "Unnamed Traveler"

print(f"""
It seems you're on your own {name}.""")

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


  print("current exits:")
  for i in exits[me['loc']].keys():
    print(abrv[i])
  
  #ask
  act = parse("do?  ")
  print()
  
  
  # handle block
  def rp(a,p):
    global act, me
    return act[0] == a and me['loc'] == p

  if act[0] in "dawk":
    me['loc'] = exits[me['loc']][act[0]]

  if rp("toggle","wr"):
    switc = not switc

  if rp("keypad","dr"):
    print("It awaits a [code <set of digits>].")
  
  if rp("code","dr"):
    if act[1] == str(code):
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
    print("give me da [key <string>]!!! >.< ")
  
  if rp("key","dkr"):
    if act[1] == (woah[::-1] + chr(121)):
      print("You feel yourself shimmer out...\nYou're free for now...")
      solved = True


print("""\n come back soon...
- NEW ROOMS!
- MORE PUZZLES!!
- A STORY MAYBE!!!""")
