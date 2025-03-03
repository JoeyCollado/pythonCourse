# sort() method = used with lists
# sort() function = used with iterables
# tuple object has no attribute of sort = ()

students = ["joey", "jake", "james", "john", "jared"]

#for sort method
#students.sort()
#students.sort(reverse=True) #sorted in reverse

#for i in students: #iterating through an object
#   print(i)

#for sort function
sorted_students = sorted(students)
#sorted_students = sorted(students,reverse=True) #reverse order

for i in sorted_students: #iterating through an object
   print(i)

