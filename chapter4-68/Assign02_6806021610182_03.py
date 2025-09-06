# 6806021610182 ณัฐวัตร จิตอารี
# 3

# รับค่าตัวเลข
num = int(input("Enter your income( -1 to exit ) : "))
# กำหนดตัวแปรเริ่มต้น
check = True
rate = 0.0
AmountTax = 0.0

# ใช้ while loop
while check:
    # เช็คค่ากรอกเข้ามาเป็น -1 ให้ แสดง Exit Program
    if num == -1:
        check = False
        print("Exit Program...")
        break
    # elif เช็คแต่ละค่าที่รับค่ามาแล้วกำหนด rate
    elif num <= 150000:
        rate = 0
    elif num <= 300000:
        rate = 2.5
    elif num <= 500000:
        rate = 4.0
    elif num <= 800000:
        rate = 5.5
    elif num < 1000000:
        rate = 7.5
    elif num >= 1000000:
        rate = 10.0
    # คำนวณ Amount Tax
    AmountTax = (num*rate)/100

# เช็ค ถ้ายังอยู่ใน Loop ให้แสดงผล
if check == True:
    print(f"Net Income : {num:,.2f}")
    print(f"Tax Rate(%) : {rate:.2f}%")
    print(f"Amount Tax : {AmountTax:,.2f}")
