#map() = applies to a function to each item in an iterable (list, tuple, etc.)
#
#map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)

store_dollars = list(map(to_euros, store))

for i in store_dollars:
    print(i)