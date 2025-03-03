# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
# ex 1
#instead of writing this function which can only use two arguments
#def add(num1,num2):
#    sum = num1 + num2
#    return sum
#
# ex 2
#do this which can accept a varying amount of arguments
def add(*args): #args = arguments
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,123))

#ex 3
#
#def add(*args): #args = arguments
#    sum = 0
#    args = list(args)
#    args[0] = 0 #change the value of the number at the index 0 which is 1 and will turn into 0
#    for i in args:
#        sum += i
#    return sum

#print(add(1,2,3,4,5,123))