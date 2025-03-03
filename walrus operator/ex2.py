#


#standard writing

#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

#using walrus

foods = list()
while food := input("What food do you like?: ") != "quit":  # (:=) = walrus, (!=) = does not
    foods.append(food)

