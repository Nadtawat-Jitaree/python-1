num = int(input("Enter number of char : "))
for row in range(1,num+1):
    for col in range(1,num+1):
        if col <= row: print("*",end="")
    print()