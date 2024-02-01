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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
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

print("You are walking through a forest and encounter a woman who asks you to guess in which "
      "hand she is carrying 'the gift of life'. Enter left or right")
answer = input()
if answer.casefold() == 'l' or answer.casefold() == 'left':
    print('The woman says "Well done. You may continue on your quest. She encourages you to move with a sharp knife."')
    print("After several hours of walking, you encounter a troll who makes it abundantly clear that you cannot "
          "cross his bridge unless you answer a riddle.")
    print('Riddle: "The poor have me; the rich need me. Eat me and you will die. What am I?"')
    answer = input()
    if answer.casefold() == "nothing":
        print('"you are right." says the troll and allows you to march over the bridge.')
        print("Eventually, some time after you have decided that this treasure is more trouble than it's worth"
              " you spot three doors which collectively take up 100% of the horizon so you must choose one of them.")
        print('Enter "red", "green" or "blue" to decide which door to choose. These aren\'t the colours of the '
              'doors, but I will know which one you mean. Note: typo means certain death and a valid choice means'
              '66.6666% chance of death. Good luck.')
        answer = input()
        if answer.casefold() == "red" or answer.casefold() == "r":
            print("Behind this door is a bottle, clearly marked as poison. Inexplicably you practically throw"
                  "it's contents down your throat and your life quickly ebbs away. Game Over!")
        elif answer.casefold() == "green" or answer.casefold() == "g":
            print("The room behind this door consists entirely of the mouth of a crocodile"
                  " who is very hungry. Game Over!")
        elif answer.casefold() == "blue" or answer.casefold() == "b":
            print("Well done! You have found the treasure. Time to go home!")
        else:
            print("This response is invalid. The penalty for this is death by being fired out"
                  " of a cannon. Game Over!")
    else:
        print('"You are wrong." says the troll. "The penalty for this is death. I will use your body organs to'
              ' fill in some potholes on my bridge". Game Over!')
else:
    print('The woman says "You are wrong!" She then proceeds to cut you up into tiny pieces. Game Over!')
