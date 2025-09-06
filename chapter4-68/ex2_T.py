MaxNum = int(input("Enter number of value(>= 1) : "))
if(MaxNum >= 1):
    MaxValue = 0
    message = ""
    for n in range(1,MaxNum+1):
        value = int(input("Enter number#"+str(n)+" : "))
        if value > MaxValue:
            MaxValue = value
            message += str(value)+" , "

    print("Your enter : ", message)
    print("Maximum value : ", MaxValue)
else:
    print("Value not correct.")

print("Exit Program")