
def find_max(a):
    Max = 0
    for i in a:
        # print(i)
        i = int(i)
        if i > Max:
            Max = i
    print(Max)

num = input("Enter your num : ")
find_max(num)