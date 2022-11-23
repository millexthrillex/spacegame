# This is the story file for the spacegame


#Beginning

import os



#class Planet:
#    def __init__(self):
#        self.name = ["Earth", "Planet 1"]
#        self.resources = ["food", "minerals"]


class Player:
    def __init__(self, name, location):
        self.location = location     #Player attributes
        self.name = name
        

    def travel():
        
    
    

player = Player(input, "Earth")



def start():
    player.name = input('Enter your name \n')
    story_1 = "Earth is in trouble. The human civilization has used up all of its resources and will only be able to survive for 65 years. Elon Musk has hired you to help him explore the galaxy and bring back energy from Proxima Centauri." 
    while True:
        
        x = name_confirm = input(f'You entered {player.name}. Confirm? \nType "yes" to confirm, "no" to return \n')  
        if x == 'yes':
            os.system('clear')
            break
        elif x == 'no':
            os.system('clear')
            return start()
        else:
            os.system('clear')
            print("I do not understand you.")
    
    print(f'Greetings {player.name}')
    print(story_1)
    while True:
        x = choice = input("Will you help save the Earth? \nType 'yes' or 'no' \n")
        if choice == 'yes':
            os.system('clear')
            print("Let's save the Earth")
            break
        elif choice == 'no':
            os.system('clear')
            print("That's too bad.")
            exit()
        else:
            os.system('clear')
            print("I do not understand you.")



if __name__ == "__main__":

    start()
    print(player.name)
    print(player.location)

    player.location = "Mars"

    print(player.location)

    player.name = "Bobby"

    print(f'Hello {player.name}')

 

    print(player.location)






            
        
        












#End

