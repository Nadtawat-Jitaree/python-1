# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_9

# กำหนดค่าเริ่มต้น
Total = 0.0
Score = ""
Count = 0

# สร้าง while กำหนดค่าถ้า Score ไม่เท่ากับ -1 ให้ loop ไปเรื่อยๆ
while Score != "-1":
    # รับค่ามา
    Score = input("Enter score value #"+str(Count+1)+" : ")
    # เช็คถ้าไม่เท่ากับ -1 ให้เพิ่ม Count +1 ไปเรื่อยๆ Total += Score ไปเรื่อยๆ
    if(Score != "-1"):
        Count += 1
        Total += float(Score)

# ปริ้นมาแสดงผล
print()
print("Number of Score : ", Count)
print("Total Score value : ", Total)
print("Average Score : ", Total/Count)