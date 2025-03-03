

students = (("jake", "F", 60),       #list of tuples
            ("joey", "S", 600),
            ("james", "A", 63),
            ("john", "C", 62),
            ("jared", "B", 61))

#sorting through list of tuples

#sorting through the first column
#students.sort()

#sorting through other columns
age = lambda ages:ages[1]
#students.sort(key=grade)
#students.sort(key=grade,reverse=True) #sorting in reverse
sorted_students = sorted(students,key=age) #sorting through tuple of tuples


#iterating
for i in sorted_students: 
    print(i)