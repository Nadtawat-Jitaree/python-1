
while True:
    h = "|  Main  Menu  |"
    print("="*len(h))
    print(h)
    print("="*len(h))
    print("1. Triangle 1")
    print("2. Triangle 2")
    print("3. Triangle 3")
    print("4. Triangle 4")
    print("5. Exit")

    choice = input("Enter Choice : ")
    num = int(input("Enter number of charactor : "))

    match choice:
        case "1":
            for i in range(num+1):
                print("*"*i)
        
            print()
        case "2":
            for i in range(num,-1,-1):
                print("*"*i)
            
            print()
        case "3":
            for i in range(num+1):
                print(" "*(num-i),"*"*i)
        
            print()
        case "4":
            for i in range(num,-1,-1):
                print(" "*(num-i),"*"*i)
        
            print()