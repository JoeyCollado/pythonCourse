def divisor(x):      #higher order function
    def dividend(y): #inner function
        return y / x
    return dividend


#variable
divide = divisor(2) #for x, x = 2
print(divide(10)) # 10 divide by 2