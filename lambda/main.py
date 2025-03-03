# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only was one expression.
#                   (think of it as a shortcut)
#                   (useful if method for a short of period of time, throw-away)

# lambda parameters:expression

#standar way of writing

#def double(x):
#    return x * 2

#print(double(5))

#

double = lambda x:x * 2
print(double(5))

#
multiply = lambda x, y: x * y
print(multiply(5,4))

#
add = lambda x,y,z: x + y + z
print(add(5,5,5))

#
fullName = lambda firstName, lastName: firstName + lastName
print(fullName("Joey ", "Collado"))