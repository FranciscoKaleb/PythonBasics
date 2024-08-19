

#[1] creating an object and printing its type Sample
print('-----------------[1]------------------')
class Sample():
    pass
my_sample_object = Sample()
print(type(my_sample_object))
#[2] Attributes and default values
print('-----------------[2]------------------')
class Dog():
    def __init__(self, mybreed = 'Askal', name = 'Kenshin', color = 'brown'):

        #Attributes
        self.breed = mybreed
        self.name = name
        self.color = color

my_dog = Dog(mybreed = 'Labrador')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)

#[3] enums class object attribute
print('-----------------[3]------------------')
from enum import Enum
# Breed(Enum) <--- this is an inheritance. Breed is an Enum
class Breed(Enum):
        Ragdoll = 'Ragdoll'
        MaineCoon = 'Maine Coon'
        Persian = 'Persian'
class Cat():
    #class object attribute
    species = 'mammal'

    def __init__(self, breed = Breed.Persian.value, name = 'ming ming', color = 'white', gender = 'female'):
        self.breed = breed
        self.name = name
        self.color = color
        self.gender = gender
my_cat = Cat(breed = Breed.MaineCoon.value, name = 'ming')
print(my_cat.species)
print(my_cat.name)
print(my_cat.breed)
print(my_cat.gender)

#[4] methods of a class
print('-----------------[4]------------------')

class Dog():
    species = 'mammal'
    def __init__(self, name = 'Brando', color = 'brown'):
        self.name = name
        self.color = color
    def bark(self):
        print('woof woof!')
    def printInfo(self):
        print(f'name: {self.name}')
        print(f'color: {self.color}')

my_dog2 = Dog()
print(my_dog2.name)
print(my_dog2.color)
my_dog2.bark()
my_dog2.printInfo()

#[5] methods of a class
print('-----------------[5]------------------')
class Circle():
    
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def get_circumference(self):
        return self.pi * self.radius * 2

my_circle = Circle(radius = 10)
num = my_circle.get_circumference()
print(num)

#[6] inheritance and polymorphism, overwriting
print('-----------------[6]------------------')
# remember in c sharp that we make a base class Abstract in order not to create an object from it
# in c++ we make a base class a pure virtual class by using = 0 so we cant create an object from it
class Animal():
    def __init__(self):
        print('Animal created')
    def whoAmI(self):
        print('I am an animal')
    def eat(self):
        print('I am eating')

class Giraffe(Animal):
    def __init__(self):
        Animal.__init__(self)     
        print('giraffe created')
    def whoAmI(self):
        print('I am a giraffe')

my_giraffe = Giraffe()
my_giraffe.eat()
my_giraffe.whoAmI()













