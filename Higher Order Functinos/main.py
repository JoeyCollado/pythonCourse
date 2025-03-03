# Higher Order Functions = a function that either:
#                          1. accepts a function as an argument
#                             or
#                          2. returns a function
#                          (In python, functions are also treated as objects)
# in python function is also treated as objects

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): #higher order function
     text = func("Hello")
     print(text)

#passing a function as an argument
hello(loud)
hello(quiet)