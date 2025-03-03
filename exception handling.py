# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("enter a number to divide: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator / denominator
#handling exception so it cannot interrupt with the flow of the program
except ZeroDivisionError as e:
    print("you can't divide by zero dumbass!")
except ValueError as e:
    print("Enter only numbers!")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:      #if no exceptions occured execute this block of code
    print(result)
finally: # whether or not we catch an exception we can always execute any code that is within our block of code for our finally clause
    print("This will always execute")