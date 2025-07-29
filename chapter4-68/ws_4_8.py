# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_8

# กำหนดค่าเริ่มต้น
Message = ""
Max = 5
Count = 1

# ใช้ while loop เมื่อ Count <= Max ให้หยุดการ Loop
while Count <= Max:
    # ใช้ S รับค่า
    S = input("Enter string #"+str(Count)+" : ")
    # ใช้ Message += S + "\n เอาตัวเลขมาต่อกัน"
    Message += S + "\n"
    # ใช้ Count + จำนวนไปเรื่อยๆเพื่อแสดงในครั้งถัดไป
    Count += 1

# ปริ้นข้อความที่รับมา
print("\nPrint your string enter : ")
print(Message)