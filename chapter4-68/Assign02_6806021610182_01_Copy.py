# 6806021610182 ณัฐวัตร จิตอารี
# 1. ให้นักศึกษาเขียนโปรแกรมรับค่าข้อมูลตัวเลขจํานวนเต็มบวก 1 ค่า จํานวนกี่หลักก็ได้ แล้วให้ทําการ ตรวจสอบว่าตัวเลขนั้นมีลักษณะเป็น Palindrome หรือไม่ พร้อมแสดงผลการเปรียบเทียบทีละคู่ โดย มีรายละเอียดการทํางานและการแสดงผลดังตัวอย่าง (ไฟล์งานชื่อ Assign02_รหัสนักศึกษา_01.py) ลักษณะ Palindrome คือ ตําแหน่งค่าของตัวที่ 1 และตัวที่ 4 เท่ากัน และตําแหน่งค่าของตัวที่ 2 และตัวที่ 3 เท่ากัน

# แสดงผลข้อความ
print(">> Program Palindrome Number <<")
# รับข้อมูล
num = input("Enter integer number : ")

# เปิด Default Str ไว้
original = ""
# loop ข้อมูลที่รับมา เก็บใส่ใน Str ที่ประกาศไว้
for ch in num:
    original = original + ch 

# ประกาศตัวแปรไว้เช็คแสดงผล palindrome เป็น true ไว้
is_palindrome = True

while True:
    # ตัวแปรเริ่มต้นให้เป็น 0
    count = 0
    # loop ข้อมูล+จำนวน count ตามจำนวน str
    for _ in original:
        count += 1
    # ถ้าเหลือน้อยกว่าหรือเท่ากับ 1 จบการเปรียบเทียบออกจาก loop
    if count <= 1:
        break

    # กำหนดตัวแปรเริ่มต้น
    first = ""
    last = ""
    i = 0
    # ดึงตัวหน้าสุดและท้ายสุด และเอาตัวแปร i +1 เพิ่มตำแหน่งไปเรื่อยๆ
    for ch in original:
        if i == 0:
            first = first + ch
        if i == count - 1:
            last = last + ch
        i += 1
    # เช็คว่า ตัวแปรกับตัวท้ายเท่ากันหรือไม่ และแสดงผล
    if first != last:
        print(f"Digit {first} not equal to Digit {last}")
        is_palindrome = False
        break
    else:
        print(f"Digit {first}  equal to Digit {last}")

    # กำหนดค่าเริ่มต้น
    new_str = ""
    j = 0
    # ตัดหัวท้ายออกเพื่อเช็คในตำแหน่งอื่นต่อ
    for ch in original:
        if j != 0 and j != count - 1:
            new_str = new_str + ch
        j += 1
    # อัปเดตข้อมูลใหม่สำหรับรอบถัดไป
    original = new_str  

# แสดงผลว่าใช่ palindrome รึป่าว
if is_palindrome:
    print(f"Your enter number : {num} is Palindrome Number.")
else:
    print(f"Your enter number : {num} is not Palindrome Number.")
# แสดงผลออกโปรแกรม
print("Exit Program")
