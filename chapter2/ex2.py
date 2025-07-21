# 6806021610182 ณัฐวัตร จิตอารี
# 2. ให้นักศึกษาเขียนโปรแกรมภาษาไพธอน เพื่อรับค่าข้อมูลตัวเลข จำนวนเต็มจำนวน 3 ค่า และหาค่าผลรวมของทั้ง 3 ค่าพร้อมแสดงผล

# รับ input ตัวเลขมา 3 จำนวน
number1 = int(input("Enter integer number 1 : "))
number2 = int(input("Enter integer number 2 : "))
number3 = int(input("Enter integer number 3 : "))

# แสดงผล ตัวเลขที่กรอกมาใน input 3 จำนวน
print("Value number 1 : ",number1)
print("Value number 2 : ",number2)
print("Value number 3 : ",number3)

# สร้างตัวแปร total มาคำนวณ บวกกันระหว่าง 3 จำนวน
total = number1+number2+number3

# แสดงผลผลรวมของจำนวนทั้ง 3
print("Total all : ",total)