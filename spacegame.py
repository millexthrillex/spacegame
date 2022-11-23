
#Beginning script of the game


#Story dialogue begins
#Class Resources
#	Food
#	Water
#	Minerals
#	Ores
#	Fuel
#	Currency
#	
#Class NPC/Trader
#	Trader 1
#	Trader 2
#	Trader 3
#	Trader 4
#	Trader 5
#	Trader 6
#	Trader 7
#	Trader 8
#
#Class Items
#	Suit
#	Energy Collection device
#	Warp Speed Upgrade 
#	Advanced Ship
##Class Time
#	Time +1 adds to Age of character
#	
#Class Character
#	Health - minimum food/water
#	Age - max 65
#	Inventory - resources/currency obtained
#	
#Class Ship
#	Fuel - amount
#	Items
#	Speed - increases with x item upgrade
#	
#			
#Class Events
#	Health - below minimum
#	Age - above 65
#	Fuel - =0
#	Resources - =0
#
#Proxima Centauri check (all 4 items)
#	Suit
#	Energy Collection device
#	Warp Speed Upgrade 
#	Advanced Ship
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
    



#user_name = input("What is your name?")
#
#Objects
#
class Planet:
    def __init__(self, name):
        self.name = name

    def planet(self, resources):
        self.recources = [food, minerals]

class Explorer:
    def __init__(self, location):
        self.location = location
        #self.name = input("What is your name? ")
    
    def travel(self, location):
        self.location = location

def travel_menu():
        print("Where would you like to travel?")
        for i in range(len(planet_list)):
            print(f'{i + 1}) {planet_list[i].name}  ')
            
        userInput = int(input())
        player.travel(planet_list[userInput - 1])
    
#	Trading Interaction
#	Collecting Interaction
#	Travelling Interaction
#	Eating/Drinking Interaction
#	Quit Interaction
#	

#        travel = input("where would you like to travel? \nPlanet1    Planet2\n")



if __name__ == "__main__":
    view_story()

    planet_list = [Planet('Earth'), Planet('Mars')]
    
    player = Explorer(planet_list[0])

    print(f'Explorer is on planet {player.location.name}')

    menu()

    print(f'Explorer is on planet {player.location.name}')

    #player.menu(int(input("What would you like to do here? \n1)Collect resources    2)Trade with NPC    3)Leave Planet\n")))

    #if player.menu([(input("What would you like to do here? \n1)Collect resources    2)Trade with NPC    3)Leave Planet\n"))]): pass
        
    
