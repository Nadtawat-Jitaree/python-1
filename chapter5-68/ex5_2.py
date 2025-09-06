# 6806021610182 ณัฐวัตร จิตอารี

from random import uniform

total = 0.0
strInput = ""
for n in range(1,6):
    num = round(uniform(30.0,50.0),2)
    total += num
    if n == 56:
        strInput += str(num)
    else:
        strInput += str(num)+" , "

print("Value Random : ",strInput)
print("Total value : ",round(total,2))
average = round(total/5,2)
print("Average value : ", round(average,2))