print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

# I like this game, but I can't figure out how to stop the game at each question if you enter the wrong answer.
# When you choose the wrong answer, the game still continues and give you the result based on whichever question you answered wrong first.
# Perhaps I will figure this out later in my coding journey!

left_right = input("Time to find your way toward Treasure Island. There's a cross road up ahead. Choose your path. Type 'left' or 'right'.\n")
swim_wait = input("You come to a lake, and you see the island in the middle of it. You also see a distant boat. Type 'wait' to wait for the boat to get you to the island. Type 'swim' to swim across the lake.\n")
door = input("You made it to the island - thank the gods. There is a house with three doors: one red, one yellow, and one blue. Which color do you choose?\n")

choice1 = left_right.lower()
choice2 = swim_wait.lower()
choice3 = door.lower()

if choice1 == "left":
  if choice2 == "wait":
    if choice3 == "yellow":
      print("You Win!")
    elif choice3 == "red":
      print("You were caught on fire when you walked through the red door. Game Over.")
    elif choice3 == "blue":
      print("The beasts behind the blue door attacked you. Game Over.")
    else:
      print("Game Over.")
  else:
    print("When you chose to swim, you were swarmed by killer trout at. Game Over.")
else:
  print("When you chose to go right at the cross roads, you fell into a hole. Game Over.")
