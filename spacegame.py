
#Beginning script of the game


#Story dialogue begins

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
    def _init__(self):
        self.planet = player.location

    def planet(self, resources):
        self.recources = [food, minerals]
#	Planet1
#	Planet2
#	Planet3
#	Planet4
#	Planet5
#	Planet6
#	Planet7
#	Planet8
	
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
#
class Explorer:
    def __init__(self):
        self.location = ['Earth', 'Mars']
        self.name = input("What is your name? ")
    
    def travel(self, location):
        self.location = ['Earth', 'Mars']

    def menu(self, action):
        self.action = ['Collect resources', 'Trade with NPC', 'Leave Planet']
#	Trading Interaction
#	Collecting Interaction
#	Travelling Interaction
#	Eating/Drinking Interaction
#	Quit Interaction
#	
#Class Time
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


#        travel = input("where would you like to travel? \nPlanet1    Planet2\n")

if __name__ == "__main__":
    view_story()

    player = Explorer()

    print(f'Explorer is on planet {player.location[0]}')
    planet_traveled_to = player.travel([int(input("where would you like to travel? \n1)Jupiter    2)Mars\n"))])
    if planet_traveled_to == player.travel([1]):
        print(f'Explorer is on planet {player.location[1]}')
    action = player.menu(int(input("What would you like to do here? \n1)Collect resources    2)Trade with NPC    3)Leave Planet\n")))
    if action == 1:
        resource = 
    
