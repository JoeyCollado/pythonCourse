# str format() = optional method that gives users
#                more control when displaying output
# format fields = function as a placeholder for a value



#animal = "cow" #1,2,3
#item = "moon" #1,2,3


#standard print statement

#print("The " +animal+" jumped over the " +item) #1

#using format method
#print("The {} jumped over the {}".format(item,animal)) #2
#print("The {1} jumped over the {0}".format(item,animal)) #positional argument #3
#print("The {item} jumped over the {item}".format(item="moon",animal="cow")) #keyword argument    


#more advance formatting
#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#adding padding, :
name = "joey"

print("Hello, my name is {:10}. Nice to meet you".format(name)) #default
print("Hello, my name is {:<10}. Nice to meet you".format(name)) #right
print("Hello, my name is {:>10}. Nice to meet you".format(name)) #left
print("Hello, my name is {:^10}. Nice to meet you".format(name)) #center

#how do we format some number variable
number1 = 3.14159
number2 = 1000

print("The number pi is {:.2f}".format(number1))
#f means floating point numbers which means it will only display two decimal portion of a floating number
print("The number pi is {:,}".format(number2)) #adds comma to every 1000+ number
print("The number pi is {:b}".format(number2)) #displaying number as binary
print("The number pi is {:0}".format(number2)) #displaying number as octonumber
print("The number pi is {:x}".format(number2)) #displaying number as hexadecimal
print("The number pi is {:e}".format(number2)) #displaying number as a scientific notation

