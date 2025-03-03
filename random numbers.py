# random module
import random

x = random.randint(1,6) #gives us random number between 1-6
y = random.random() #gives us random number between 0-1

#rock paper scissor
myList =['rock','paper','scissors'] #give random string usling list
z = random.choice(myList)

#shuffle method
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(cards)