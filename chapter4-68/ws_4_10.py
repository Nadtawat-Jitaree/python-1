# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_10


# สร้างตัวแปรเริ่มต้น
Done = True
Count = 0

# สร้าง While Loop
while Done:
    # รับค่า input เข้ามา
    Score = input("Enter score value #"+str(Count+1)+" : ")
    # ถ้า Score ไม่เท่ากับ -1 ให้เข้าเงื่อนไข
    if Score != "-1":
        # ตัวแปร Mart รับค่า Score แปลงเป็น float
        Mark = float(Score)
        # ถ้า Mark มากว่าหรือเท่ากับ 0 และ Mark น้อยกว่าหรือเท่ากับ 100 ให้เข้าเงื่อนไข
        if Mark >= 0 and Mark <= 100:
            # สร้างตัวแปรเริ่มต้น
            Grade = ""
            # ถ้า Mark มากกว่าหรือเท่ากับ 80 ให้แสดงเกรด A
            if Mark >= 80:
                Grade = "A"
            # ถ้า Mark มากกว่าหรือเท่ากับ 70 ให้แสดงเกรด B
            elif Mark >= 70:
                Grade = "B"
            # ถ้า Mark มากกว่าหรือเท่ากับ 60 ให้แสดงเกรด C
            elif Mark >= 60:
                Grade = "C"
            # ถ้า Mark มากกว่าหรือเท่ากับ 50 ให้แสดงเกรด D
            elif Mark >= 50:
                Grade = "D"
            # ถ้านอกเหนือจากนั้นให้แสดงเกรด F
            else:
                Grade = "F"
            
            # ปริ้นค่า คะแนนออกมา แล้วบอกเกรด
            print("Score is "+str(Mark)+", get"+Grade)
            # Count สร้างนับจำนวนครั้งโดย +1 ไปเรื่อยๆ
            Count += 1
        else:
            # นอกจากเงื่อนไขนี้แล้วให้กรอกคะแนนอีกครั้ง
            print("Score out of range , input again ")
    # ถ้ากรอก -1 ให้ออกจาก loop
    elif Score == "-1":
        Done = False

# ออกจากโปรแกรม
print("Exit Program")