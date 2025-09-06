def factoraial1(number):
    fac = 1
    for n in range(1,number+1):
        fac = fac * n
    return(fac)

def factoraial2(number):
    if number > 0:
        return(number * factoraial2(number - 1))
    else:
        return(1)
    
num = int(input("Enter number : "))
print("Factorial1 with for = ",factoraial1(num))
print("Factorial2 with recursive = ",factoraial2(num))
