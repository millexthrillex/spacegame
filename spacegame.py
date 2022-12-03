import os
import random
#Beginning script of the game


#Story dialogue begins
#Class Resources
#   Food
#   Water
#   Minerals
#   Ores
#   Fuel
#   Currency
#   
#Class NPC/Trader
#   Trader 1
#   Trader 2
#   Trader 3
#   Trader 4
#   Trader 5
#   Trader 6
#   Trader 7
#   Trader 8
#
#Class Items
#   Suit
#   Energy Collection device
#   Warp Speed Upgrade 
#   Advanced Ship
##Class Time
#   Time +1 adds to Age of character
#   
#Class Character
#   Health - minimum food/water
#   Age - max 65
#   Inventory - resources/currency obtained
#   
#Class Ship
#   Fuel - amount
#   Items
#   Speed - increases with x item upgrade
#   
#           
#Class Events
#   Health - below minimum
#   Age - above 85
#   Fuel - =0
#   Resources - =0
#
#Proxima Centauri check (all 4 items)
#   Suit
#   Energy Collection device
#   Warp Speed Upgrade 
#   Advanced Ship
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





def start():
    clr()
    print(f"""{bcolors.OKCYAN}{bcolors.BOLD}
:::     ::: :::::::::: :::::::::  ::::::::::: :::::::::: ::::::::::: :::::::::: :::::::::       :::::::::: :::    ::: :::::::::  :::        ::::::::  :::::::::  :::::::::: :::::::::       ::: 
:+:     :+: :+:        :+:    :+:     :+:     :+:            :+:     :+:        :+:    :+:      :+:        :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+:        :+:    :+:      :+: 
+:+     +:+ +:+        +:+    +:+     +:+     +:+            +:+     +:+        +:+    +:+      +:+         +:+  +:+  +:+    +:+ +:+       +:+    +:+ +:+    +:+ +:+        +:+    +:+      +:+ 
+#+     +:+ +#++:++#   +#++:++#:      +#+     :#::+::#       +#+     +#++:++#   +#+    +:+      +#++:++#     +#++:+   +#++:++#+  +#+       +#+    +:+ +#++:++#:  +#++:++#   +#++:++#:       +#+ 
 +#+   +#+  +#+        +#+    +#+     +#+     +#+            +#+     +#+        +#+    +#+      +#+         +#+  +#+  +#+        +#+       +#+    +#+ +#+    +#+ +#+        +#+    +#+      +#+ 
  #+#+#+#   #+#        #+#    #+#     #+#     #+#            #+#     #+#        #+#    #+#      #+#        #+#    #+# #+#        #+#       #+#    #+# #+#    #+# #+#        #+#    #+#          
    ###     ########## ###    ### ########### ###        ########### ########## #########       ########## ###    ### ###        ########## ########  ###    ### ########## ###    ###      ### 
        



        {bcolors.ENDC}""")
    player.name = input(f'{bcolors.BOLD}What is your Twitter handle?\n{bcolors.ENDC}')
   
    
    story_1 = (f"{bcolors.OKBLUE}Earth is in trouble. The human civilization has slowly but surely been killing the Earth and it is estimated to die in 65 years. Elon Musk needs your help to explore the galaxy for a special mission in order to restore the Earth's core energy.{bcolors.ENDC}")
    while True:
        
        x = name_confirm = input(f'You entered {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}. Is this correct? \nType "yes" to confirm, "no" to return. \n')  
        if x == 'yes':
            clr()
            break
        elif x == 'no':
            clr()
            return start()
        else:
            clr()
            print("I do not understand you.")
    
    print(f'Greetings {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}')
    print(story_1)
    while True:
        x = choice = input("Will you help save the Earth? \nType 'yes' or 'no' \n")
        if choice == 'yes':
            clr()
            input(f"""{bcolors.OKGREEN}Let's save the Earth!{bcolors.ENDC}\n""")
            input("""Your mission, should you choose to accept it, is to explore the planets within the galaxy and acquire special items needed to travel to Proxima Centauri.\nIn order to get there, you will need a super heat-resistant space suit, an advanced ship, and the warp speed ship upgrade. Proxima Centauri has a special type of energy within. Perhaps you may also need something to collect the energy with...\n""")
            clr()
            input("Now that you know your mission, your adventure has just begun.\nYou find yourself within Twitter headquarters on Earth. So, tell me explorer...\n")
            break
        elif choice == 'no':
            clr()
            print(f"{bcolors.FAIL}That's too bad.{bcolors.ENDC}")
            exit()
        else:
            clr()
            print(f"{bcolors.WARNING}I do not understand you.{bcolors.ENDC}")

    
def clr():
    clr = os.system('clear')
    return clr

def check_age():
    if player.age >= 85:
        input(f"{bcolors.FAIL}You are 85 years old. Mission Failed.\nGame Over{bcolors.ENDC}")
        exit()

def check_fuel():
    if inventory[3].quantity < 0:
        input(f"""{bcolors.FAIL}You are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





            {bcolors.ENDC}""")
        exit()

def check_game_over():
    check_age()
    check_fuel()

def travel_menu():
    clr()
    print(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} is on planet {player.location.name}')
    print("Enter the number of the planet you would like to travel?")
    for i in range(len(planet_list)):
        print(f'{i + 1}) {planet_list[i].name}  ')

    try:
        
        userInput = int(input())
        x = 0
    
        if userInput == 1 and inventory[3].quantity >= 1:   # Travel to Earth
            if player.location.name == planet_list[1].name: # From Mars
                player.age += 11.78/52
                inventory[3].quantity -= 1
                x = 1
                check_game_over()
            if player.location.name == planet_list[2].name: # From Neptune
                player.age += 668.06/52
                inventory[3].quantity -= 67
                x = 67
                check_game_over()
            if player.location.name == planet_list[3].name: # From Jupiter 
                player.age += 94.53/52
                inventory[3].quantity -= 10
                x = 10
                check_game_over()
            if player.location.name == planet_list[4].name: # From Proxima Centauri
                player.age += 423.57/52
                inventory[3].quantity -= 42
                x = 42
                check_game_over()
            if player.location.name == planet_list[5].name: # From Proxima Centauri
                player.age += 423.57/52
                inventory[3].quantity -= 42
                x = 42
                check_game_over()
                
    
    
        if userInput == 2 and inventory[3].quantity >= 1:  # Travel to Mars
            if player.location.name == planet_list[0].name: # From Earth
                player.age += 11.78/52
                inventory[3].quantity -= 1
                x = 1
                check_game_over()
            if player.location.name == planet_list[2].name: # From Neptune
                player.age += 642.49/52
                inventory[3].quantity -= 64
                x = 64
                check_game_over()
            if player.location.name == planet_list[3].name: # From Jupiter
                player.age += 82.76/52
                inventory[3].quantity -= 8
                x = 8
                check_game_over()
            if player.location.name == planet_list[4].name: # From Uranus
                player.age += 397.79/52
                inventory[3].quantity -= 40
                x = 40
                check_game_over()
    
            if player.location.name == planet_list[5].name: # From Proxima Centauri
                player.age += 0/52
                inventory[3].quantity -= 0
                x = 0
                check_game_over()
    
        if userInput == 3 and inventory[3].quantity >= 1:  # Travel to Neptune
            if player.location.name == planet_list[0].name: # From Earth
                player.age += 654.27/52
                inventory[3].quantity -= 65
                x = 65
                check_game_over()
            if player.location.name == planet_list[1].name: # From Mars
                player.age += 642.49/52
                inventory[3].quantity -= 64
                x = 64
                check_game_over()
            if player.location.name == planet_list[3].name: # From Jupiter
                player.age += 559.73/52
                inventory[3].quantity -= 56
                x = 56
                check_game_over()
            if player.location.name == planet_list[4].name: # From Uranus
                player.age += 244.70/52
                inventory[3].quantity -= 25
                x = 25
                check_game_over()
            if player.location.name == planet_list[5].name: # From Proxima Centauri
                player.age += 0/52
                inventory[3].quantity -= 0
                x = 0
                check_game_over()
    
        if userInput == 4 and inventory[3].quantity >= 1:  # Travel to Jupiter
            if player.location.name == planet_list[0].name: # From Earth 
                player.age += 94.53/52
                inventory[3].quantity -= 10
                x = 10
                check_game_over()
            if player.location.name == planet_list[1].name: # From Mars
                player.age += 82.76/52
                inventory[3].quantity -= 8
                x = 8
                check_game_over()
            if player.location.name == planet_list[2].name: # From Neptune
                player.age += 559.73/52
                inventory[3].quantity -= 56
                x = 56
                check_game_over()
            if player.location.name == planet_list[4].name: # From Uranus
                player.age += 315.03/52
                inventory[3].quantity -= 32
                x = 32
                check_game_over()
            if player.location.name == planet_list[5].name: # From Proxima Centauri
                player.age += 0/52
                inventory[3].quantity -= 0
                x = 0
                check_game_over()
    
        if userInput == 5 and inventory[3].quantity >= 1:  # Travel to Uranus
            if player.location.name == planet_list[0].name: # From Earth 
                player.age += 409.57/52
                inventory[3].quantity -= 41
                x = 41
                check_game_over()
            if player.location.name == planet_list[1].name: # From Mars 
                player.age += 397.79/52
                inventory[3].quantity -= 40
                x = 41
                check_game_over()
            if player.location.name == planet_list[2].name: # From Neptune 
                player.age += 244.7/52
                inventory[3].quantity -= 25
                x = 25
                check_game_over()
            if player.location.name == planet_list[3].name: # From Jupiter 
                player.age += 315.03/52
                inventory[3].quantity -= 32
                x = 32
                check_game_over()
            if player.location.name == planet_list[4].name: # From Proxima Centauri 
                player.age += 0/52
                inventory[3].quantity -= 0
                x = 0
                check_game_over()

        if userInput == 6 and inventory[3].quantity >= 1:  # Travel to Proxima Centauri
            if player.location.name == planet_list[0].name: # From Earth
                if inventory[5].quantity == 1 and inventory[6].quantity == 1 and inventory[7].quantity == 1 and inventory[8].quantity == 1:
                    player.age += 1200/52
                    inventory[3].quantity -= 120
                    x = 120
                    check_game_over()
                    good_ending()
                else:
                    clr()
                    print('''You do not have the required special items... \nYou are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





                        ''')
                    quit()
            if player.location.name == planet_list[1].name: # From Mars
                if inventory[5].quantity == 1 and inventory[6].quantity == 1 and inventory[7].quantity == 1 and inventory[8].quantity == 1: 
                    player.age += 1202/52
                    inventory[3].quantity -= 120
                    x = 120
                    check_game_over()
                    good_ending()
                else:
                    clr()
                    print('''You do not have the required special items... \nYou are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





                        ''')
                    quit()
            if player.location.name == planet_list[2].name: # From Neptune 
                if inventory[5].quantity == 1 and inventory[6].quantity == 1 and inventory[7].quantity == 1 and inventory[8].quantity == 1: 
                    player.age += 1320/52
                    inventory[3].quantity -= 130
                    x = 130
                    check_game_over()
                    good_ending()
                else:
                    clr()
                    print('''You do not have the required special items... \nYou are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





                        ''')
                    quit()
            if player.location.name == planet_list[3].name: # From Jupiter 
                if inventory[5].quantity == 1 and inventory[6].quantity == 1 and inventory[7].quantity == 1 and inventory[8].quantity == 1: 
                    player.age += 1210/52
                    inventory[3].quantity -= 121
                    x = 121
                    check_game_over()
                    good_ending()
                else:
                    clr()
                    print('''You do not have the required special items... \nYou are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





                        ''')
                    quit()
            if player.location.name == planet_list[4].name: # From Uranus
                if inventory[5].quantity == 1 and inventory[6].quantity == 1 and inventory[7].quantity == 1 and inventory[8].quantity == 1: 
                    player.age += 1255/52
                    inventory[3].quantity -= 126
                    x = 126
                    check_game_over()
                    good_ending()
                else:
                    clr()
                    print('''You do not have the required special items... \nYou are out of fuel. You spend the next couple of years floating in space and eventually die...\n

 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 





                        ''')
                    quit()





                
           
        player.travel(planet_list[userInput - 1])
        print(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} is on planet {player.location.name}.\n{x} fuel used.')
        Mug_event()
        input()
    except (ValueError, IndexError):
        input('You never made up your mind and went back to base.')
        
def good_ending():
    clr()
    player.location = planet_list[0].name
    input(f'After traveling for many years, you finally reach Proxima Centauri. Having all of the special items granted you the ability to use your Auger to retrieve the energy. You make your journey back home and restore Earth back to normal. Elon Musk is pleased, congratulations {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}, you are now verified on Twitter!')
    clr()
    
    quit()
    

def menu():
    clr()
    print(f'What would you like to do on {player.location.name}? ')
    print('1)Gather resources \n2)Travel \n3)View inventory \n4)Trade \n5)Quit Game')
    try:
        userInput = int(input())
        if userInput == 1:
            gather_resources()
        elif userInput == 2:
            travel_menu()
        elif userInput == 3:
            view_inv()
        elif userInput == 4:
            Trade()
        elif userInput == 5:
            x = input("Are you sure you want to quit?\nType 'yes' to quit\n")
            if x == "yes":
                quit()
        else:
            input(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}! That is not a valid option.')
    except(ValueError, IndexError):
        input('It seems you partied too much last night, come back later.')

def view_inv():
    while True:
        clr()
        print(f'Inventory:                                              {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}\'s age: {int(player.age)}')
        for i in range(len(inventory)):
            if inventory[i].quantity != 0:
                print(f'{inventory[i].name} x{inventory[i].quantity}')
        e = input('Enter to return to Menu.\n')
        if e == '':
            break
        else:
            continue
           
        
def Trade():
        clr()
        print(f'Good day {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}! Here is what I have to offer.\n')

         
        for i in range(len(items_list) - 1):
            ran_num = random.choice(range(1, 10))
            token_ran_num = random.choice(range(1, 10))
            npc_inv[i].quantity = ran_num
            npc_inv[4].quantity = token_ran_num
            print(f'{i + 1}) {ran_num}x {items_list[i].name} for {token_ran_num}x space tokens\n' )
            if i == 0:
                npc_inv[5].quantity = token_ran_num
            elif i == 1:
                npc_inv[6].quantity = token_ran_num
            elif i == 2:
                npc_inv[7].quantity = token_ran_num
            elif i == 3:
                npc_inv[8].quantity = token_ran_num
        if player.location == planet_list[1]:
            if inventory[5].quantity == 0:
                print(f'5) 50x Space Tokens for 1x Special Suit')
        if player.location == planet_list[2]:
            if inventory[6].quantity == 0:
                print(f'5) 50x Space Tokens for 1x Energy Collection Device')
        if player.location == planet_list[3]:
            if inventory[7].quantity == 0:
                print(f'5) 50x Space Tokens for 1x Warp Speed Upgrade')
        if player.location == planet_list[4]:
            if inventory[8].quantity == 0:
                print(f'5) 50x Space Tokens for 1x Advanced Ship')
        print('What would you like to trade? \n')

        try:
            y = True
            userInput = int(input())
         
            if player.location == planet_list[1]:
                if userInput == 5:
                    if inventory[4].quantity >= 50:
                        if inventory[5].quantity == 0:
                            inventory[5].quantity = 1
                            inventory[4].quantity -= 50
                            y = False
                            input(f"Congrats {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}, you have acquired a Special Item \nThis special suit will help withstand the heat of Proxima Centaury")
                        else:
                            input('If you are not gonna make a trade, leave!')
                    else:
                        input('You do not have enough tokens!')
    
            if player.location == planet_list[2]:
                if userInput == 5:
                    if inventory[4].quantity >= 50:
                        if inventory[6].quantity == 0:
                            inventory[6].quantity = 1
                            inventory[4].quantity -= 50
                            y = False
                            input(f"Congrats {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}, you have acquired a Special Item \nThis special suit will help withstand the heat of Proxima Centaury")
                        else:
                            input('If you are not gonna make a trade, leave!')
                    else:
                        input('You do not have enough tokens!')
                     
            if player.location == planet_list[3]:
                if userInput == 5:
                    if inventory[4].quantity >= 50:
                        if inventory[7].quantity == 0:
                            inventory[7].quantity = 1
                            inventory[4].quantity -= 50
                            y = False
                            input(f"Congrats {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}, you have acquired a Special Item \nThis special suit will help withstand the heat of Proxima Centaury")
                        else:
                            input('If you are not gonna make a trade, leave!')
                    else:
                        input('You do not have enough tokens!')
                     
            if player.location == planet_list[4]:
                if userInput == 5:
                    if inventory[4].quantity >= 50:
                        if inventory[7].quantity == 0:
                            inventory[8].quantity = 1
                            inventory[4].quantity -=50
                            y = False
                            input(f"Congrats {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}, you have acquired a Special Item \nThis special suit will help withstand the heat of Proxima Centaury")
                        else:
                            input('If you are not gonna make a trade, leave!')
                    else:
                        input('You do not have enough tokens!')
                     
            if userInput <= 4:
                if inventory[userInput - 1].quantity >= npc_inv[userInput - 1].quantity:
                    inventory[4].quantity += npc_inv[userInput + 4].quantity
                    inventory[userInput - 1].quantity -= npc_inv[userInput - 1].quantity
                    print(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} traded {npc_inv[userInput - 1].quantity}x {npc_inv[userInput - 1].name} for {npc_inv[userInput + 4].quantity}x {npc_inv[4].name}')
                    input()
                    
            else:
                if y == True:
                    input('The trader looks at you in disgust and kicks you out of his store.')
        except (ValueError, IndexError):
                input('The trader looks at you in disgust and kicks you out of his store.')
                 
        Mug_event()
    
class Planet:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self,location, age = 20):
        self.location = location
        self.name = 'name'
        self.age = age
        
    def travel(self, location):
        self.location = location


class Item:
    def __init__(self, name, quantity = 0):
        self.name = name
        self.quantity = quantity

def gather_resources():
    clr()

    print(f'What would you like to gather from {player.location.name}? ')

    for i in range(len(items_list)-1):
        print(f'{i + 1}) {items_list[i].name}')

    try:
        userInput = int(input())
        if userInput > 4 or userInput < 1:
            input(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}! That is not an option.')

        else:
    
            items_list[userInput - 1].quantity = random.choice(range(1, 11))

            inventory[userInput - 1].quantity += items_list[userInput - 1].quantity
    
    
            print(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} has gathered {inventory[userInput - 1].name} x{items_list[userInput - 1].quantity}')
            player.age = player.age + (1/52)
    
            print('One week has passed')    

            Mug_event()
            input()

    except(ValueError):
        input(f'{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} is triggered and will try again later.')
        
def Mug_event():
    ran_num = random.choice(range(1,101))
    if ran_num in range(60, 66):
        input("OH NO! A raider is trying to mug you.")
        input(f"""{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC}{bcolors.FAIL} tried to fend off the raider, but inevitibly got pummeled to the ground.{bcolors.ENDC} \n{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} {bcolors.FAIL}is now poor and can't continue the adventure. \nBetter luck next time!{bcolors.ENDC}
{bcolors.FAIL}
 ::::::::      :::     ::::    ::::  ::::::::::       ::::::::  :::     ::: :::::::::: :::::::::  
:+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:             :+:    :+: :+:     :+: :+:        :+:    :+: 
+:+         +:+   +:+  +:+ +:+:+ +:+ +:+             +:+    +:+ +:+     +:+ +:+        +:+    +:+ 
:#:        +#++:++#++: +#+  +:+  +#+ +#++:++#        +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:  
+#+   +#+# +#+     +#+ +#+       +#+ +#+             +#+    +#+  +#+   +#+  +#+        +#+    +#+ 
#+#    #+# #+#     #+# #+#       #+# #+#             #+#    #+#   #+#+#+#   #+#        #+#    #+# 
 ########  ###     ### ###       ### ##########       ########      ###     ########## ###    ### 
{bcolors.ENDC}




            """)
        quit()
    if ran_num < 11:
        input("OH NO! A raider is trying to mug you.")
        input(f"{bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} tried to fend off the raider, and somehow was successful. After a few minutes, {bcolors.BOLD}{bcolors.OKGREEN}{player.name}{bcolors.ENDC} returned to base.")
            


if __name__ == "__main__":
    planet_list = [Planet('Earth'), Planet('Mars'), Planet('Neptune'), Planet('Jupiter'), Planet('Uranus'), Planet('Proxima Centauri')]
                
    player = Player(planet_list[0])
    
    items_list = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens')]

    inventory = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens'), Item('Suit'), Item('Energy Collection device'), Item('Warp Speed Upgrade'), Item('Advanced Ship')]

    npc_inv = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens'), Item('space tokens1'), Item('space tokens2'), Item('space tokens3'), Item('space tokens4')]

    sp_item_list = [Item('Suit'), Item('Energy Collection device'), Item('Warp Speed Upgrade'), Item('Advanced Ship')]

    inventory[3].quantity = 11
    inventory[4].quantity = 0
    inventory[5].quantity = 0
    inventory[6].quantity = 0
    inventory[7].quantity = 0
    inventory[8].quantity = 0
    #start()


    while True:
        menu()