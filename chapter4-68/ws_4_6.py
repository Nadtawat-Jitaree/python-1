# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_6

# รับค่าตัวเลข
Num = int(input("Enter max number : "))

# ใช้ loop ตั้งแต่ 1 ถึง Num+1
for  n in range(1,Num+1):
    # หารเอาเศษ ถ้าหารเอาเศษแล้วเศษเป็น 0 จะเท่ากับเลขคู่
    if n % 2 == 0:
        print(f"{n} is even number")
    # นอกจากนั้นจะเป็นเลขคี่
    else:
        print(f"{n} is odd number")