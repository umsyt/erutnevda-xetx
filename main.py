import random
code = random.randint(1000,9999)
solved = False
switc = False

def parse(quer):
  inp = input(quer)
  act = inp.split(" ")
  return act

me = {"loc": "cr"}
exits = {"cr":{"d" : "dr", "w": "wr"},
        "dr":{"d" : "wr", "w": "cr"},
        "wr":{"d" : "cr", "w": "dr"}}
desc = {"cr":"A dark, seemingly dingy room. You can make out a screen.",
        "wr":"Also dark. There seems to be a switch which you can [toggle].",
        "dr":"A [keypad] and a door."}
abrv = {"d": "[d]eosil",
        "w": "[w]iddershins",
        "a": "[a]na",
        "k": "[k]ata"}

print("""
BRAINDOWN: THE INTERACTIVE FRICTION
v.0.0.2 (three rooms?)
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
      print("The door opens...\nYou are free!\n for now...")
      solved = True
    else:
      print("The keypad gives a curt beep.")
  


print("""\n come back soon...
- NEW ROOMS!
- MORE PUZZLES!!
- A STORY MAYBE!!!""")
