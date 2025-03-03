class Animal:

    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    #overriding a method
    def eat(self):
        print("this rabbit is eating a carrot") # specific implementation

rabbit = Rabbit()
rabbit.eat()

#method overriding = is the ability of an object oriented programming language to allow a subclass to provide
#                    a specific implementation of a method that is already provided by one of its parents

