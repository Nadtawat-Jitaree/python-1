# 6806021610182 ณัฐวัตร จิตอารี
# WorkShop 4_4

import math

fnum = float(input("Enter float number : "))

print()
print("Ceil number : ", math.ceil(fnum))
print("Floor number : ", math.floor(fnum))
print("Sqrt number : ", math.sqrt(fnum))
print("Trunc number : ", math.trunc(fnum))

num = math.trunc(fnum)
print("Degree Angle : ",num)
print("Radians Angle : ", math.radians(num))
print("sin : ", math.sin(math.radians((num))))
print("cos : ", math.cos(math.radians((num))))
print("tan : ", math.tan(math.radians((num))))