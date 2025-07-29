# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_1

# รับค่า int มา 2 ค่า
baseInt = int(input('ใส่ค่าเลขฐานจำนวนเต็ม : '))
expInt = int(input('ใส่ค่ายกกำลังจำนวนเต็ม : '))
# pow(ค่าฐาน,ค่ายกกำลัง) x**3
result = pow(baseInt,expInt)
# แสดงผล
print("ค่ายกกำลังของ",baseInt,'^',expInt,' = ',result)
print()
# รับค่า float มา 2 ค่า
basefloat = float(input('ใส่ค่าเลขฐานจำนวนทศนิยม : '))
expfloat = float(input('ใส่ค่ายกกำลังจำนวนทศนิยม : '))
# pow(ค่าฐาน,ค่ายกกำลัง) x**3
result = pow(basefloat,expfloat)
# แสดงผล
print("ค่ายกกำลังของ ",basefloat,'^',expfloat,end='')
# round ใช้ในการปัดเศษ round(ตัวเลข,[จำนวนทศนิยม])
print(' = ', result , "->",round(result,2))