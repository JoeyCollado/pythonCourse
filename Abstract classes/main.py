# abstract classes = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod #import abstract method



class Vechile(ABC):

    @abstractmethod #this will prevent us to create an object out of the vechile class losing a physical form kind of like a ghost
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):
    def go(self):
        print("you drive the car")

    #to inherit a method from the parent class that is now an abstract we need to override the method and provide its own implementation
    def stop(self):
        print("you stop the car")

class Motorcycle(Vechile):
    def go(self):
        print("you drive the motorcycle")

    def stop(self):
        print("you stop the motorcycle")


#vechile = Vechile() #can no longer create a vechile object coz it has been turned abstract
car = Car()
motorcycle = Motorcycle()

#vechile.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()