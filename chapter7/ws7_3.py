def display_triangle(num,ch):
    for n in range(1,num+1):
        message = ""
        for m in range(n):
            message += ch
        print(message)

print("Program display triangle.")
num = int(input("Enter number line : "))
ch  = input("Enter character : ")
display_triangle(num,ch)