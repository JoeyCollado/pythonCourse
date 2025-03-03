# logical operators = (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("what is temperature?:"))

if temp>=0 and temp <=30: # and logical operator, both condition needs to be true
    print("the temperature is nice")

elif temp < 0 or temp >30: # or logical operator, its either too hot or too cold, if temp less than 0 its cold if temp is greter than 30 its hot, as long as one condition is true, the statement is true
    print("the temperatur is bad")

#elif not(temp>=0 and temp <=30):# not logical operator, if condition is true it will be flipped to false vice versa
    #print("temperature is weird")







