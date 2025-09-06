# 6806021610182 ณัฐวัตร จิตอารี
# Chapter 4 ข้อ 2

# แสดงผลข้อความ
print(">> Program Find Maximum Value <<")
# รับค่า int จำนวนค่าที่จะรับ
number = int(input("Enter number of value(>= 1) : "))
# ถ้าน้อยกว่าหรือเท่ากับ 0 ให้แสดง Value input not correct
if number <= 0:
    print("Value input not correct.")
    print("Exit Program")
else:
    numbers = []
    # แสดงจำนวนที่จะต้องกรอก
    print("Program get value ",number,"numbers.")
    #  Loop ตามจำนวน
    for n in range(number):
        # รับค่า num มา
        num = input(f"Enter value Number #{n+1} : ")
        # เก็บเข้า Array ตัวแปร numbers โดยใช้ append(ข้อมูล)
        numbers.append(num)

    # แสดงผลข้อความด้วย join map str ด้วยตัวแปร เพื่อแสดงข้อความใน Array
    print("Your enter number : ",' , '.join(map(str,numbers)))
    # แสดงค่ามากสุดในตัวแปร numbers
    print("Maximum value number is ",max(numbers))
    print("Exit Program")