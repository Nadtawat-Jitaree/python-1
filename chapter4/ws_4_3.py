# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_3

# รับค่า input ตัวอักษรมารับแค่ 1 ตัวอักษร
ch = input("Enter character : ")

# แสดงผลตัวอักษรที่รับมา
# ord แปลงค่าอักขระเป็น Ascii
print("Character ", ch, " has ascii value ",ord(ch))
# chr แปลงค่า Ascii เป็น ord
print("Ascii value ",ord(ch), " has character value ", chr(ord(ch)))
print()
# สร้างตัวแปรกำหนดค่าให้แปลงค่า Ascii
num = ord(ch)

# แสดงผลค่าที่แปลงเป็น Ascii
print("Decimal value : ", num)
# แสดงผลค่า Binary
print("Binary value : ", bin(num))
# แสดงผลค่า Octal
print("Octal value : ", oct(num))
# แสดงผลค่า Hexa
print("Hexa value : ", hex(num))
