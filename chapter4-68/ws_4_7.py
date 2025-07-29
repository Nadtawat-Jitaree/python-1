# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_7

# เริ่มต้นค่า total
total = 0.0
# รับค่า int มากำหนดค่า score ที่จะรับสูงสุดกี่จำนวน
Max = int(input("Enter number of score : "))

# ใช้ for loop range(เริ่มต้น,สิ้นสุดกับค่าที่รับมา)
for n in range(1,Max+1):
    # สร้างตัวแปรรับค่า float มา
    score = float(input("Enter Score #"+str(n)+" : "))
    # นำ total มาเก็บค่า total + score ไปเรื่อยๆ
    total = total + score

print()
# แสดงผล total score
print("Total score value : ", total)
