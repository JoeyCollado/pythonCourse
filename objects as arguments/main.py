# passing objects as arguments

class Car: #class

    color = None

class Motor: #class

    color = None


def change_color(car,color): #function

    car.color = color

#creating objects
car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motor()
#

#calling the function
change_color(car1, "red")
change_color(car2, "green")
change_color(car3, "blue")
change_color(bike1, "white") #the function was reused by another class

#

#display
print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)

#