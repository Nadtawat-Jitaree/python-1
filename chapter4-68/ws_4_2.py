# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_2

# รับค่า int มา 4 ค่า
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))
num4 = int(input("Enter Number 4 : "))

# กำหนดค่า Max ให้มีค่า = 0
Max = 0
# if เช็คถ้าค่า Max น้อยกว่า num1 ที่รับค่ามาให้ค่า Max = num1
if Max < num1:
    Max = num1
# if เช็คถ้าค่า Max(ค่าnum1) น้อยกว่า num2 ที่รับค่ามาให้ค่า Max = num2
if Max < num2:
    Max = num2
# if เช็คถ้าค่า Max(ค่าnum1หรือnum2) น้อยกว่า num3 ที่รับค่ามาให้ค่า Max = num3
if Max < num3:
    Max = num3
# if เช็คถ้าค่า Max(ค่าnum1หรือnum2หรือnum3) น้อยกว่า num4 ที่รับค่ามาให้ค่า Max = num4
if Max < num4:
    Max = num4

# แสดงผลค่ามากสุดของตัวเลข 4 จำนวน
print("\nMaximum number value : ",Max)