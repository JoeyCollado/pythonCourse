# if statement = a block of code that will execute if its condition is true

age = int(input("How old are you?"))

if age == 100:
    print("You are Century old:")
elif age >= 18:
    print("you are an adult:")
elif age < 1:
    print("you don't exist:")
else:
    print("you are a child:")