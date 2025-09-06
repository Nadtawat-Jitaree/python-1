# 6806021610182 ณัฐวัตร จิตอารี

baseInt = int(input("ใส่ค่าเลขฐานจำนวนเต็ม : "))
expInt = int(input("ใส่ค่ายกกำลังจำนวนเต็ม : "))
result = pow(baseInt,expInt)
print("ค่ายกกำลังของ ",baseInt,"^",expInt," = ",result)
print()

basefloat = float(input("ใส่ค่าเลขฐานจำนวนทศนิยม : "))
expfloat = float(input("ใส่ค่ายกกำลังจำนวนทศนิยม : "))
result = pow(basefloat,expfloat)
print("ค่ายกกำลังของ ",basefloat,"^",expfloat,end="")
print(" = ", result , "->",round(result,2))