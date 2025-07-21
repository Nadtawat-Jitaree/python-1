# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 3_1

# รับค่าจำนวนสินค้า
qty = int(input("Enter number product : "))
# รับค่าราคาสินค้า
price = float(input("Price per unit : "))

# คำนวนราคา
total = price * qty 
# แสดงผลราคา
print("Total money : ",total)

# กรอกจำนวนเงินที่จะจ่าย
pay = float(input("Enter pay money : "))
# คำนวนเงินทอน
change = pay - total
# แสดงผลเงินทอน
print("Money change : ", change)