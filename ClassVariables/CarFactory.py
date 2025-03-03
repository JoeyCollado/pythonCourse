#object = is an instance of a class by using programming we can create representations of real life objects
#         using programming we can mimic real world objects by assigning a combination of attributes (ex. name,age,height) what the objects look like
#                                                                                         or methods (ex.eat,sleep) what the object do
from Car import Car

car_1 = Car("chevy","corvette","2021","blue") #we need matching set of arguments to make it work, in this case the matching sets or argument is make,model,year,color
car_2 = Car("ford","mustang","2024","red") #creating the 2nd object

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
#calling the methods
car_1.drive()
car_1.stop()

#printing the 2nd car
#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.color)

#car_2.drive()
#car_2.stop))