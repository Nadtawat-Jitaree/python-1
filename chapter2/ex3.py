# 6806021610182 ณัฐวัตร จิตอารี
# 3. ให้นักศึกษาเขียนโปรแกรมภาษาไพธอน เพื่อรับค่าข้อมูลทศนิยม จำนวนเต็มจำนวน 3 ค่า และหาค่าผลรวมของทั้ง 3 ค่าพร้อมแสดงผล

# กรอกจำนวนทศนิยม 3 จำนวน
number1 = float(input("Enter float number 1 : "))
number2 = float(input("Enter float number 2 : "))
number3 = float(input("Enter float number 3 : "))

# แสดงผล ทศนิยมที่กรอกมาใน input 3 จำนวน

print("Value number 1 : ",number1)
print("Value number 2 : ",number2)
print("Value number 3 : ",number3)

# สร้างตัวแปร total มาคำนวณ บวกกันระหว่าง 3 จำนวน
total = number1+number2+number3

# แสดงผลผลรวมของจำนวนทั้ง 3 ที่เป็น float
print("Total all : ",total)