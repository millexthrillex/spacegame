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
#   Age - above 65
#   Fuel - =0
#   Resources - =0
#
#Proxima Centauri check (all 4 items)
#   Suit
#   Energy Collection device
#   Warp Speed Upgrade 
#   Advanced Ship
def start():
    player.name = input('Enter your name\n')
    
    story_1 = "Earth is in trouble. The human civilization has used up all of its resources and will only be able to survive for 65 years. Elon Musk has hired you to help him explore the galaxy and bring back energy from Proxima Centauri." 
    while True:
        
        x = name_confirm = input(f'You entered {player.name}. Confirm? \nType "yes" to confirm, "no" to return \n')  
        if x == 'yes':
            clr()
            break
        elif x == 'no':
            clr()
            return start()
        else:
            clr()
            print("I do not understand you.")
    
    print(f'Greetings {player.name}')
    print(story_1)
    while True:
        x = choice = input("Will you help save the Earth? \nType 'yes' or 'no' \n")
        if choice == 'yes':
            clr()
            print("Let's save the Earth")
            break
        elif choice == 'no':
            clr()
            print("That's too bad.")
            exit()
        else:
            clr()
            print("I do not understand you.")

story_list = []

def open_list():
    global story_list
    try:
        with open('story.txt', mode = 'r') as f:
            b = f.readlines()
            story_list = [x.replace('\n', '') for x in b]
    except FileNotFoundError:
        open(story.txt, w)


def view_story():
    open_list()
    for i in range(len(story_list)):
        user_input = input((story_list[i]))
    
def clr():
    clr = os.system('clear')
    return clr

def travel_menu():
    clr()
    print(f'Explorer is on planet {player.location.name}')
    print("Enter the number of the planet you would like to travel?")
    for i in range(len(planet_list)):
        print(f'{i + 1}) {planet_list[i].name}  ')

    userInput = int(input())
    if userInput == 2:
        if player.location.name == planet_list[0].name:
            player.age += 11.78/52

    if userInput == 1:
        if player.location.name == planet_list[1].name:
            player.age += 11.78/52
            
    
    player.travel(planet_list[userInput - 1])
    print(f'Explorer is on planet {player.location.name}')
    

    
def menu():
    clr()
    print(f'What would you like to do in {player.location .name}? ')
    print('1)Gather resources \n2)Travel \n3)View inventory \n4)Trade')
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

def view_inv():
    while True:
        clr()
        print(f'Inventory:                Explorer\'s age: {int(player.age)}')
        for i in range(len(inventory)):
            if inventory[i].quantity != 0:
                print(f'{inventory[i].name} x{inventory[i].quantity}')
        e = input('Enter to return to Menu\n')
        if e == '':
            break
        else:
            continue
        

        
        
def Trade():
     clr()
     print(f'What would you like to trade? \n')

     #U_input = inter(input())
     
     for i in range(len(items_list) - 1):
         ran_num = random.choice(range(1, 10))
         token_ran_num = random.choice(range(1, 10))
         npc_inv[i].quantity = ran_num
         npc_inv[4].quantity = token_ran_num
         print(f'{i + 1}) {ran_num}x {items_list[i].name} for {token_ran_num}x space tokens\n' )
         if i == 0:
             npc_inv[5].quantity = token_ran_num
         if i == 1:
             npc_inv[6].quantity = token_ran_num
         if i == 2:
             npc_inv[7].quantity = token_ran_num
         if i == 4:
             npc_inv[8].quantity = token_ran_num

     userInput = int(input())
     if inventory[userInput - 1].quantity >= npc_inv[userInput - 1].quantity:
         inventory[4].quantity += npc_inv[userInput + 4].quantity
         inventory[userInput - 1].quantity -= npc_inv[userInput - 1].quantity
         print(f'You traded {npc_inv[userInput - 1].quantity}x {npc_inv[userInput - 1].name} for {npc_inv[userInput +4].quantity}x {npc_inv[4].name}')
         input()

     
    
class Planet:
    def __init__(self, name):
        self.name = name

    def planet(self, resources):
        self.resources = resources

        

class Player:
    def __init__(self,location, inventory = [], age = 20):
        self.location = location
        self.name = 'name'
        self.inventory = []
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

    userInput = int(input())

    if userInput > 4 or userInput < 1:
        input('Not an option')

    else:
    
        items_list[userInput - 1].quantity = random.choice(range(1, 10))

        inventory[userInput - 1].quantity += items_list[userInput - 1].quantity
    
    
        print(f'Explorer has gathered {inventory[userInput - 1].name} x{items_list[userInput - 1].quantity}')
        player.age = player.age + (1/52)
    
        print('One week has passed')
        input()    


            

    
#   Trading Interaction
#   Eating/Drinking Interaction
#   Quit Interaction
#   Time



if __name__ == "__main__":
    planet_list = [Planet('Earth'), Planet('Mars')]
                
    player = Player(planet_list[0])
    
    items_list = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens')]

    inventory = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens')]

    npc_inv = [Item('food'), Item('minerals'), Item('water'), Item('fuel'), Item('space tokens'), Item('space tokens1'), Item('space tokens2'), Item('space tokens4'), Item('space tokens4')]

    inventory[3].quantity = 10


    
    #start()


    while True:
        menu()

    #player.menu(int(input("What would you like to do here? \n1)Collect resources    2)Trade with NPC    3)Leave Planet\n")))
#
    #if player.menu([(input("What would you like to do here? \n1)Collect resources    2)Trade with NPC    3)Leave Planet\n"))]): pass