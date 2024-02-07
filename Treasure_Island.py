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
name = input("Enter your name: ")
print(f"Hi,{name}.Welcome to Treasure Island 🏝️.")
print("Your mission is to find the treasure 💰.")
direction = input("You are on the end of a road showing left and right directions. Now you have to choose 'left' or 'right': ").lower()

if direction == "left":
    decision = input("You have come to a river. Now either you have to swim or wait for a boat to cross the river. What would you like to do? 'swim' or 'wait': ")
    if decision == "swim":
        print("""             .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'""")
        print("You swam across a river and eaten by crocodiles🐊.")
    elif decision == "wait":
        print("""
                   ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^""")
        colour = input("You crossed the river by a boat and entered into an island. You walked and saw a house with three doors which arein red, blue, yellow colours. Now choose the door of your wish: ").lower()
        if colour == "red":
            print("""⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
                ⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
                ⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
                ⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
                ⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
                ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
                ⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
                ⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
                ⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀ """)
            print("You entered into a room with full of fire🔥. You lose👎")
        elif colour == "blue":
            print("""
                          .-=-.          .--.
              __        .'     '.       /  " )
      _     .'  '.     /   .-.   \     /  .-'\
     ( \   / .-.  \   /   /   \   \   /  /    ^
      \ `-` /   \  `-'   /     \   `-`  /
    jgs`-.-`     '.____.'       `.____.'
""")
            
            print("There is a poisonous snake🐍 inside the room. It bit you and you died. You lose.👎")
        elif colour == "yellow":
            print("You found the Treasure💰successfully 🥳 and you went back to home with that treasure annd lived your life happily.")
        else:
            print("Invalid response.")
    else:
        print("Invalid option.")

elif direction == "right":
    print(""" ⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀
⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀""")
    print("You have walked and entered into a jungle, suddenly a lion attacked and killed you.🦁")
else:
    print("Invalid option.")
