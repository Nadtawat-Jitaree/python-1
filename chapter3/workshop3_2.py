# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 3_2

# รับค่าจำนวนที่ 1
num1 =  int(input("Enter number 1 : "))
# รับค่าจำนวนที่ 2
num2 =  int(input("Enter number 2 : "))
# แสดงผลก่อนสลับตำแหน่ง
print("Before swap num1 = ", num1,", num2 = ", num2)
# เอาจำนวนที่ 1 + 2 แล้วเอาค่า num2 รับค่าไว้
num2 = num1 + num2
# เอา num1 กำหนดค่าให้ num2 - num1
num1 = num2 - num1
# เอา num2 กำหนดค่าให้ num2 - num1
num2 = num2 - num1

# แสดงผลหลังสลับตำแหน่ง
print("Alter swap num1 = ", num1,", num2 = ", num2)
