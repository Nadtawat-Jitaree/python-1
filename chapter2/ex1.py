# 6806021610182 ณัฐวัตร จิตอารี
# 1. ให้นักศึกษาเขียนโปรแกรมภาษาไพธอน รับค่าชื่อ นามสกุล และอายุ แล้วนำข้อมูลมาแสดงผลหน้าจอ แสดงผลตามตัวอย่างและคำนวณอายุเมื่อนักศึกษาในอีก 4 ปีข้างหน้า
# รับค่า input ชื่อ สกุล อายุ
name = str(input("Enter name: "))
surname = str(input("Enter surname: "))
age = int(input("Enter age: "))

# เอาตัวแปรที่กำหนดค่ามาแสดงผล
print("My name is", name)
print("My surname is", surname)
print("Now I'm ", age , "years old")

# เอา age มาแสดงผลโดยคำนวณ +4 ให้แสดงอายุตอนจบอีก 4 ปีข้างหน้า
print("I'll Finish undergraduate in",age+4,"years old")
