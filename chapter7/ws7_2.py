def sum_number(End):
    sum = 0
    for n in range(1,End+1):
        sum += n
    print(f"sum of 1 .. {End} = {sum}")

print("Program sum 1 to n used function. ")
num = int(input("Enter number : "))
sum_number(num)