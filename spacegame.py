
# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
 
# Class for Dog
 
 
class Planet:
 
    # Class Variable
    planet = 'planet'
 
    # The init method or constructor
    def __init__(self, name, resources):
 
        # Instance Variable
        self.name = [Earth, Venus]
        self.resources = [Ore, Gold]
 
 
# Objects of Dog class
Earth = Planet("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Earth details:')
print('Earth is a', Earth.planet)
print('name: ', Earth.name)
print('resources: ', Earth.resources)
 
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
