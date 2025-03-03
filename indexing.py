# index operator [] = gives across to a sequence's element (str,list,tuples)

name = "joey collado"

# 1st example
#if (name[0].islower()):
#    name = name.capitalize()

#print(name) #checks if first letter on the string is lowercase if not the variable will be re assigned and change the first letter to capital
#2nd example


first_name = name[0:4].upper()#create a substring of first name
last_name = name[5:].lower() #create a substring of last name, we leave the second index empty because we dont need to know the end, it will print everything from index 5 to end
last_character = name[-1] #print last character of the element

print(first_name)
print(last_name)
print(last_character)

