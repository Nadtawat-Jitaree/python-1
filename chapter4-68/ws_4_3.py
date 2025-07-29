# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_3

# รับค่า int มา 3 ค่า
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

# ถ้า num1 มากกว่า num2
if num1 > num2:
    # ให้เช็คต่อว่า num1 มากกว่า num3 ไหม
    if num1 > num3:
        # ถ้าใช่ให้ Max = num1
        Max = num1
    else:
        # ถ้าไม่ให้ Max = num3
        Max = num3
# หลังจากนี้
else:
    # ถ้า num2 มากกว่า num3
    if num2 > num3:
        # ให้ Max = num2
        Max = num2
    else:
        # นอกจากนั้นให้ Max = num3
        Max = num3

# แสดงผลค่ามากสุดของตัวเลข 3 จำนวน
print("\nMaximum number value : ",Max)