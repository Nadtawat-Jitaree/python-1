# 6806021610182 ณัฐวัตร จิตอารี
# import math as m
from math import log10
# eq1
# x = float(input("Enter angle : "))

# rad = math.radians(x)
# eq1 = pow(math.sin(rad),2)*pow(math.cos(rad),2)
# print("Eq 1 = ", round(eq1,4))

# eq2
# x = float(input("Enter angle : "))
# rad = m.radians(x)
# eq2 = m.exp(0.5*m.sqrt(m.tan(m.cos(rad))))
# print("Eq2 = ",round(eq2,4))

# eq3 0.ขึ้นไป ไม่เกิน 1
x = float(input("Enter float : "))
eq3 = log10(pow(x,2)/(1-x))/pow(x,5+x)
print("Eq2 = ",round(eq3,4))