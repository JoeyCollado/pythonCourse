# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created

name = "joey"        #global scope (available inside and outside of functions as it is declared outside) 

def display_name():
    name = "collado"   #local scope (Available only inside this function)
    print(name)  #prints local
 

display_name()
print(name)  #prints global

#this concept follows the LEGB concept which is LOCAL ENCLOSING GLOBAL BUILT IN

