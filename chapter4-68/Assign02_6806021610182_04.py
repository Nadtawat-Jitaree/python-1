# 6806021610182 ณัฐวัตร จิตอารี
# 4

# ประกาศตัวแปรเริ่มต้น
check = True
sum = 0
sumOdd = 0
sumEven = 0
# ใช้ while loop
while check:
    # แสดงผล
    print("="*23)
    print("::     Main Menu     ::")
    print("="*23)
    print(" A. Get Integer Number")
    print(" B. Summation of Digit")
    print(" C. Count Digit")
    print(" D. Exit")

    # รับค่าเพื่อเลือก choice
    choice = input("Enter Choice : ")
    # เช็คถ้าค่าที่รับมาเป็น A หรือ a ให้รับค่า num มา
    if  choice == "A" or choice == "a":
        num = input("\nEnter long number : ")
        print("")
    # เช็คถ้าค่าที่รับมาเป็น B หรือ b ให้คำนวณหาผลรวมของจำนวณคู่และคี่
    elif choice == "B" or choice == "b":
        print("Your enter number : ",num)
        # ใช้ for loop คำนวณผลรวม
        for n in num:
            sum += int(n)
            # ใช้ if เช็คว่ามีเศษไหม ถ้ามีก็เป็น เลขคี่
            if int(n) % 2:
                sumOdd += int(n)
            # ถ้าไม่มีก็เป็นเลขคู่
            else:
                sumEven += int(n)
        # แสดงผล
        print("Summation of digit : ",sum)
        print("Summation odd of digit : ",sumOdd)
        print("Summation even of digit : ",sumEven,"\n")

    # เช็คถ้าค่าที่รับมาเป็น C หรือ c แสดงจำนวนหลักที่รับค่าเข้ามา
    elif choice == "C" or choice == "c":
        print("\nYour enter number : ",num)
        print("This number has ",len(num)," digits.\n")
    # เช็คถ้าค่าที่รับมาเป็น D หรือ d ออกจาก loop จบโปรแกรม
    elif choice == "D" or choice == "d":
        check = False
        print("\nExit Program...")
    