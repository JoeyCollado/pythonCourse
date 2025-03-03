#loop control statements = Change a loop execution from its normal sequence

#break    = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass     = does nothing, acts as a placeholder

# break example, here you need to enter your name to exit the loop or else you will be stuck
#while True:
#    name = input("enter your name")
#    if name != "":
#        break
#
# continue example,
#phone_number = "123-456-7890"
#for i in phone_number: #for each character within the string of the phone_number
#    if i == "-": #if index is equal to - which is the iteration we place on the index will be skipped and continued the rest of the string
#        continue
#    print(i,end="")
#
# pass example, does nothing it acts as a placeholder
for i in range(1,21): # i = will iterate the number 1-20
    
    if i == 13: # if i runs into 13 or equal to 13
        pass    # program will pass it and skipped
    else:         
        print(i) 
      