# 6806021610182 ณัฐวัตร จิตอารี

from math import sin, cos, tan, log, sqrt

x = float(input("Enter your X : "))

ex1 = (sin(x)**2) * (cos(x)**2)
ex2 = (1/2) * sqrt(tan(cos(x)))
ex3 = log((x**2) / (1 - x)) / (x**(5 + x))

print("ex1 is:", ex1)
print("ex2 is:", ex2)
print("ex3 is:", ex3)
