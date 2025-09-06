# 6806021610182 ณัฐวัตร จิตอารี
# 2

# แสดงผล
print(">> Program Change Number to Text <<")
# รับค่า
num = input("Enter integer number : ")

# แสดงค่าตัวเลขที่นับมา
print("Number : ", num)

# กำหนดตัวแปรเริ่มต้น str
num_str = ""
# loop ข้อมูลตาม num
for n in num:
    # ใช้if ว่า = ตัวเลขนั้นๆไหมแล้ว += ไปเรื่อยๆ
    if n == "0":
        num_str += "Zero "
    elif n == "1":
        num_str += "One "
    elif n == "2":
        num_str += "Two "
    elif n == "3":
        num_str += "Three "
    elif n == "4":
        num_str += "Four "
    elif n == "5":
        num_str += "Five "
    elif n == "6":
        num_str += "Six "
    elif n == "7":
        num_str += "Seven "
    elif n == "8":
        num_str += "Eight "
    elif n == "9":
        num_str += "Nine "

# แสดงข้อความ
print("Text : ",num_str)
print("Exit Program")
