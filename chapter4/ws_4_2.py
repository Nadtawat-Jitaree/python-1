# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_2

# รับค่า int มา 3 ค่า
num1 = int(input("Enter value number1 : "))
num2 = int(input("Enter value number2 : "))
num3 = int(input("Enter value number3 : "))

# หาค่าตัวเลขที่น้อยที่สุด
MinValue = min(num1 , num2, num3)

# หาค่าตัวเลขที่มากที่สุด
MaxValue = max(num1 , num2, num3)

print()
# แสดงค่าที่กรอก 3 ค่า
print("Your enter number : ", num1, num2, num3)
# แสดงผลค่าสูงสุด
print("Maximum value : ", MaxValue)
# แสดงผลค่าต่ำสุด
print("Minimum value : ", MinValue)

# round ใช้ในการปัดเศษ round(ตัวเลข,[จำนวนทศนิยม])
# sum หาผลรวมของตัวเลข
print("Average value : ",round(sum((num1, num2, num3))/3,2))
# ปัดเศษ(หาผลรวม(ค่าที่1,ค่าที่2,ค่าที่3/3,2ตำแหน่ง))