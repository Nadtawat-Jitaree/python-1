# 6806021610182 ณัฐวัตร จิตอารี
# Chapter 4 ข้อ 1

# case 1
# สร้างตัวแปรมา
# Done = True
# # แสดงผล
# print(" >> Program Find Maximun Digit << ")
# # Loop ตัวแปรที่เป็นจริง
# while Done:

#     # รับค่าข้อมูลเป็น int
#     number = int(input("Enter integer number(0-exit) : "))
#     # เช็คถ้ากรอกมาเป็น 0 ให้ออกจากโปรแกรม
#     if number == 0:
#         Done = False
#         print("Exit Program")
#     # นอกเหนือจากนั้นให้หาค่ามากสุดของตัวเลขโดยใช้ max(map(int, str(ตัวแปร))) map int เป็น str ก่อน
#     else:
#         maxDigi = max(map(int , str(number)))
#         # แสดงผล
#         print("Maximum Digit of interger  number",number,"=",maxDigi)

# case 2
# สร้างตัวแปรมา
Done = True
# แสดงผล
print(" >> Program Find Maximun Digit << ")
# Loop ตัวแปรที่เป็นจริง
while Done:

    # รับค่าข้อมูล
    number = input("Enter integer number(0-exit) : ")
    # เช็คถ้ากรอกมาเป็น 0 ให้ออกจากโปรแกรม
    if number == '0':
        Done = False
        print("Exit Program")
    # นอกเหนือจากนั้นให้หาค่ามากสุดของตัวที่กรอกมาเป็น str max(ตัวแปร)
    else:
        maxDigi = max(number)
        # แสดงผล
        print("Maximum Digit of interger  number",number,"=",maxDigi)
