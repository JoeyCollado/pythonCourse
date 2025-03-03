#tuple = collection which is ordered and unchangeable  
#        used to group together related data

student = ("joey" ,21, "male")

print(student.count("joey")) #checks and count the element specified on the index
print(student.index("male")) #checks and count the element specified on the index

for x in student: #prints all value on the tuple
    print(x)

if "joey" in student: #checks to see if the value is in the tuple if true it will print the following below
    print("joey is Here:")