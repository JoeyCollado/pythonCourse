#reduce = apply a function to an iterable and reduce it to a single cumulative value.
#         performs function on first two elements and repeats process until 1 value remains
#
#reduce(function,iterable)

import functools

#ex 1
#letters = ("H","E","L","L","O")
#word = functools.reduce(lambda x,y,:x + y,letters)
#print(word)


#ex 2
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x * y,factorial)
print(result)