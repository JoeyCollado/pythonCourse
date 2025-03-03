#nested loop = a loop inside a loop
#              the inner loop will finish all its iterations before executing the iterations on the outer loop

rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("Enter symbol?: ")

for i in range(rows): #inner loop
    for j in range(columns): #outer loop
        print(symbol, end="") # end="" = prevents cursor from moving down to the next line 
    print()