# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 3_4

# แสดงผลข้อความ
print("Program Calculate Area Circle.")
# รับค่า circle radius
radius = float(input("Enter circle radius (float number) : "))
# คำนวณหาพื้นที่วงกลม
area = 3.14 * radius * radius
# หาพื้นที่เส้นรอบวง
circum = 2 * 3.14 * radius

# แสดงผล
print("Area of circle with radius", radius,"is",area)
print("Circumference is ",circum)