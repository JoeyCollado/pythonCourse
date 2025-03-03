# zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,etc.)
#                  creates a zip object with paired elemnents stored in tuples for each element within our zip object

#            tuples
usernames = ["Dude", "Bro", "Mister"] #iterables
passwords = ["pass", "123", "word"] #iterables

#       converting zip object to dictionary
users = dict(zip(usernames, passwords)) #zip elements together between two iterables and pair them to each other, This is zip object

print(type(users))

for key,value in users.items():
    print(key+" : "+value)