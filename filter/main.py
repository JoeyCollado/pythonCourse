# filter() = creates a collection of elements from an iterable for which a function returns
#
# filter(function,iterable)

friends = [("joey", 19),
           ("jake", 23),
           ("john", 43),
           ("james", 54),
           ("jay", 66),
           ("jared", 86)]


#lambda function
age = lambda data:data[1] >= 18

#filter the elements using the function
drinking_buds = list(filter(age, friends))

#iterating through the array
for i in drinking_buds:
    print(i)