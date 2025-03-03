# list comprehension = a way to create new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

students = [100,90,80,70,60,50,40,30,20,10,0]

#                             function           iterable

#passed_students = list(filter(lambda x: x >= 60, students))

#passed_students = [i for i in students if i >=60]

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)
