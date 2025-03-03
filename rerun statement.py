# rerun statement = functions send python values/objects back to the caller
#                   these values/objects are known as the function's return value

def multiply(number1,number2): #creating a function
    result = number1 * number2 #result will be = number1 * number2
    return result #returns result to the caller

x = multiply(6,8) #store the result to the variable x

print(x) #prints result by calling variable x