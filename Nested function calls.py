# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

#num = input("enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)

#print(num)

#way of writing code with less line
print(round(abs(float(input("enter a whole positive number: "))))) #the same thing above but in just one line of code
                                                                   #we resolve first with innermost function then next is the outer function and so on