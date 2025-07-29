# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_4

# รับค่า int เข้ามา
score = int(input("Enter socre : "))

# เช็คถ้าค่าที่รับมา มากกว่า 100 หรือ ค่าที่รับมา น้อยกว่า 0 ให้แสดงข้อความแจ้งเตือน
if score > 100 or score < 0:
    print("Score not in range")
# เช็คค่าที่รับมาถ้ามีค่าน้อยกว่าหรือเท่ากับ 80,70,60,50,0 ให้แสดงคะแนนที่กรอก และเกรดที่ได้
elif score >= 80 and score <= 100:
    print("Score value ",score,", got grade A")
elif score >= 70 and score <= 79:
    print("Score value ",score,", got grade B")
elif score >= 60 and score <= 69:
    print("Score value ",score,", got grade C")
elif score >= 50 and score <= 59:
    print("Score value ",score,", got grade D")
elif score >= 0 and score <= 49:
    print("Score value ",score,", got grade F")
else:
    # นอกจากนี้ให้แสดงข้อความเกิดข้อผิดพลาด
    print("error")