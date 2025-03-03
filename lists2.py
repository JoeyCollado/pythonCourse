#2nd demonstration of the lesson

food = ["pizza","burger","taco","shawarma","cake"]

food[0] = "sushi"
#methods
food.append("ice cream") #replace element
food.remove("pizza") #remove element
food.pop() #remove last element
food.insert(0,"nigga") #add element
food.sort() #sort list alphabetically
food.clear() #remove all elements on the list

for x in food:
    print(x)