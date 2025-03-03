#set = collection which is unordered , unindexed, no duplicate values

utensils = {"spoon", "fork", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#useful methods
#utensils.add("napkin") #add elements to the set
#utensils.remove("spoon") #removes elements to the set
#utensils.clear() #removes all elements to the set
#utensils.update(dishes) #add all elements on the dishes set to the utensils set
#dinner_table = utensils.union(dishes) #join two sets to create a new sets altogether

#compare elements
#print(dishes.difference(utensils))  #checks to see if there's a different element on two different sets
print(utensils.intersection(dishes)) #checks to see if there's a common element on two different sets

#for x in dinner_table:
#    print(x)