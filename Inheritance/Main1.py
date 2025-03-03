class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")
#     child | parent class, the child class will inherit all methods of the parent class
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")
class Fish(Animal):
    def swim(self):
        print("This Fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

#create 3 objects
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#attributes and methods inherited from the parent class
print(Rabbit.alive)
fish.sleep()
hawk.eat()

#attributes and methods of the child class
rabbit.run()
fish.swim()
hawk.fly()