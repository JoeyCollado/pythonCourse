#dictionary comprehension = creates dictionaries using an expression
#                           can replace for loops and certain lambda functions
#
#dictionary = {key: expression for (key:value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
#dictionary = {key: (if/else) for (key,value) in iterable}
#dictionary = {key: function(value) for (key,value) in iterable}
#

#ex1

#cities_in_f = {'new york': 32, 'boston': 75, 'los angeles':100, 'chicago': 50}
#cities_in_c = {key: round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
#print(cities_in_c)

#ex2

#cities_in_f = {'new york': 32, 'boston': 75, 'los angeles':100, 'chicago': 50}
#desc_cities = {key: ("WARM" if value >=40 else "COLD") for (key,value) in cities_in_f.items()}
#print(desc_cities)

#ex3

#defining a function
def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69>= value >=40:
        return "WARM"
    else:
        return "COLD"
#
cities_in_f = {'new york': 32, 'boston': 75, 'los angeles':100, 'chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities_in_f.items()}