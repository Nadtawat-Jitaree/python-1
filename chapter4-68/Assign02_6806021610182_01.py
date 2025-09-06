# 6806021610182 ณัฐวัตร จิตอารี
# 1. ให้นักศึกษาเขียนโปรแกรมรับค่าข้อมูลตัวเลขจํานวนเต็มบวก 1 ค่า จํานวนกี่หลักก็ได้ แล้วให้ทําการ ตรวจสอบว่าตัวเลขนั้นมีลักษณะเป็น Palindrome หรือไม่ พร้อมแสดงผลการเปรียบเทียบทีละคู่ โดย มีรายละเอียดการทํางานและการแสดงผลดังตัวอย่าง (ไฟล์งานชื่อ Assign02_รหัสนักศึกษา_01.py) ลักษณะ Palindrome คือ ตําแหน่งค่าของตัวที่ 1 และตัวที่ 4 เท่ากัน และตําแหน่งค่าของตัวที่ 2 และตัวที่ 3 เท่ากัน

# แสดงผลข้อความ
print(">> Program Palindrome Number <<")
# รับข้อมูล
num = input("Enter integer number : ")

# ประกาศตัวแปรไว้เช็คแสดงผล palindrome เป็น true ไว้
is_palindrome = True
# คำนวณความยาวของตัวเลข - 1 ใช้เป็น index ด้านขวา
lenNum = len(num)-1

# loop
for i in range(lenNum):
    # เปรียบเทียบตำแหน่งซ้ายสุดกับขวาสุด = กันไหม
    if num[i] == num[lenNum-i]:
        # แสดงข้อความ
        print(f"Digit {num[i]} equal to Digit {num[lenNum-i]}")
    else:
        # ถ้าไม่เท่ากันให้กำหนดตัวแปรบอกไม่ใช่ palindrome
        is_palindrome = False
        # แสดงข้อความ
        print(f"Digit {num[i]} not equal to Digit {num[lenNum-i]}")
        break

# แสดงผลว่าใช่ palindrome รึป่าว
if is_palindrome:
    print(f"Your enter number : {num} is Palindrome Number.")
else:
    print(f"Your enter number : {num} is not Palindrome Number.")
# แสดงผลออกโปรแกรม
print("Exit Program")
