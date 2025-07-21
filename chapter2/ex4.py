# 6806021610182 ณัฐวัตร จิตอารี
# 4. ให้นักศึกษาเขียนโปรแกรมภาษาไพธอน เพื่อคำนวณหาพื้นที่ของรูปสี่เหลี่ยมพื้นผ้า โดยมีการรับค่าความยาวและความกว้างเป็นตัวเลขจำนวนเต็มมีรูปแบบการทำงานตามตัวอย่าง

# แสดงผลข้อความ
print("Program Calculate Area Rectangle.")

# รับค่า Length กับ Width มาจาก input
Length = float(input("Enter Length : "))
Widht = float(input("Enter Widht : "))

# สร้างตัวแปร cal มาคำนวณหาพื้นที่ 3 เหลี่ยมโดยเอากว้างคูณยาว
cal = Length*Widht

# แสดงผลพื้นที่ของรูปสามเหลี่ยม
print("Area of Rectangle = ",cal)