# 6806021610182 ณัฐวัตร จิตอารี
import random

a = random.randint(1,10)
print("random value 1 , 10 = ", a)
a = random.randint(40,100)
print("random value 40 , 100 = ", a,"\n")
b = random.random()
print("random float value 0.000 - 0.999 = ",b , "\n")
c = random.uniform(1.5,8.5)
print("c = ",c,"\n")
d = random.choice("Python")
print("random data from specific = ",d , "\n")
e = random.randrange(10,101,10)
print("random 10 - 100 step 10 = ",e)