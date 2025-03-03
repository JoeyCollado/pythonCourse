# method chaining = is used to call multiple methods sequentially   
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("you stop the engine")
        return self                     #needs this line of code to use method chaining

#create an object
car = Car()

#calling methods using method chaining

#car.turn_on().drive()                  #calling turn on method and drive method sequentially

#car.brake().turn_off()



#car.turn_on().drive().brake().turn_off()   #calling all method

#alternative writing
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()