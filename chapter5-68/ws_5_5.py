# 6806021610182 ณัฐวัตร จิตอารี

import math
num1 = int(input("Enter integer number1 : "))
num2 = int(input("Enter integer number2 : "))
gcdNum = math.gcd(num1,num2)
lcmNum = math.lcm(num1,num2)
print()
print("Integer number ", num1 , " and ", num2)
print("Greatest Common Divisor = ",gcdNum)
print("Least Common Multiple = ",lcmNum)
print()
print("Factorial ", num1 , "! is value ",math.factorial(num1))
print("Factorial ", num2 , "! is value ",math.factorial(num2))