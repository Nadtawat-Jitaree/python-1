# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_5

# แสดงผลข้อความ
print("Show Menu\n================")
# แสดงผลข้อความเมนูให้ลือกใช้
print("1. Menu 1\n2. Menu 2\n3. Menu 3\n4. Exit")

# กำหนดตัวแปรรับค่า Choice ให้กรอก
choice = input("Enter Choice : ")

# ใช้ match หรือ switch case เหมือนภาษา c
# match ตัวแปรที่รับค่ามา
match choice:
    # ถ้าค่าเป็น 1 ให้แสดงข้อความ Choose 1
    case '1':
        print('Choose 1')
    # ถ้าค่าเป็น 2 ให้แสดงข้อความ Choose 2
    case '2':
        print('Choose 2')
    # ถ้าค่าเป็น 3 ให้แสดงข้อความ Choose 3
    case '3':
        print('Choose 3')
    # ถ้าค่าเป็น 4 ให้แสดงข้อความ Choose 4
    case '4':
        print('Choose 4')
    # นอกเหนือจากนี้ให้แสดง Error no choice
    case _ :
        print('Error no choice')