# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter, unlike positional arguments
#                     python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="Joey",last="Collado",middle="Aibert")
