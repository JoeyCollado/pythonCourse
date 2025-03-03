#Slicing = create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]

name = "JoeyPogi"

first_name = name[0:4]
last_name = name[4:8]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)