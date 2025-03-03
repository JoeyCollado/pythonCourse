import os

path = "C:\\Users\\akosi\\OneDrive\\Desktop\\Python"

if os.path.exists(path): #check if path file location exist on my computer
    print("That Location exists!")
    if os.path.isfile(path):   #check if file is a file
        print("that is a file")
    elif os.path.isdir(path): #check if file is a folder/directory
        print("that is a folder/directory")
else:
    print("That location doesn't exist!")
