# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present 
#               "if it walks like a duck and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("The duck is talking")

    def talk(self):
        print("The duck is walking")

class Chicken:

    def walk(self):
        print("The chicken is talking")

    def talk(self):
        print("The chicken is walking")

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")

#creating objects
duck = Duck()
chicken = Chicken()
person = Person()

#
person.catch(duck)
person.catch(chicken) #this works even though we dont have a chicken parameter because the chicken class have similar methods to duck
