import random
code = random.randint(1000,9999)
solved = False

print("""
BRAINDOWN: THE INTERACTIVE FRICTION
v.0.0.1 (one room build)
Welcome, dear traveler to-
to...
Honestly, I don't know where.
""")

name = input("What would you like to call yourself? ")

if name == "":
  name = "Unnamed Traveler"

print(f"""
It seems you're on your own {name}.

You are in a dark room with a [panel] and [keypad] in front of you.""")

while not solved:
  inp = input("what would you like to do? ")
  act = inp.split(" ")
  if act[0] == "panel":
    print(f"It's a panel with the number {code} on it.")
  if act[0] == "keypad":
    print("It awaits a [code <digits>]")
  if act[0] == "code":
    if str(code) == act[1]:
      print("you've entered it right! you're free!")
      solved = True
    else:
      print("wrong code...")

print("""\n come back soon...
- NEW ROOMS!
- MORE PUZZLES!!
- A STORY MAYBE!!!""")
