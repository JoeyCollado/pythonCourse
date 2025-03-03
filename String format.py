# str format() = optional method that gives users
#                more control when displaying output
# format fields = function as a placeholder for a value


animal = "cow" #1,2,3
item = "moon" #1,2,3


#standard print statement

#print("The " +animal+" jumped over the " +item) #1

#using format method
#print("The {} jumped over the {}".format(item,animal)) #2
#print("The {1} jumped over the {0}".format(item,animal)) #positional argument #3
#print("The {item} jumped over the {item}".format(item="moon",animal="cow")) #keyword argument    


#more advance formatting
text = "The {} jumped over the {}"
print(text.format(animal,item))
