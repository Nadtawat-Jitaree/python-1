# 6806021610182 ณัฐวัตร จิตอารี

import math as m

fnum = float(input("Enter float number : "))
print()
print("Ceil number : ",m.ceil(fnum))
print("Floor number : ",m.floor(fnum))
print("Sqrt number : ",m.sqrt(fnum))
print("Trunc number : ",m.trunc(fnum))

num = m.trunc(fnum)
print("Degree Angle : ",num)
print("Radians Angle : ",m.radians(num))
print("sin : ",m.sin(m.radians(num)))
print("cos : ",m.cos(m.radians(num)))
print("tan : ",m.tan(m.radians(num)))