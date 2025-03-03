# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs): #keyword arguments = kwargs
    #print("hello" + kwargs['first'] + " " + kwargs['last'])
    #ways to iterate a full name using kwargs
    #
    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title="god",first=" joey", middle="ugale", last="collado")

