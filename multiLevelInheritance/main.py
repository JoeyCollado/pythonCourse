#multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism: #parent class

    alive = True

class Animal(Organism): #child class inherits from the parent class

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #multi-level inheritance as this child class inherits from another derived child class (Animal)
    
    def bark(self):
        print("This dog is barking")

#create object
dog = Dog()

#call methods
print(dog.alive)
dog.eat()
dog.bark()