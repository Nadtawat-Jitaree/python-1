import math
print()

h = "|Angle|    Sin    |   Cos   |   Tan   |"
print("="*len(h))
print(h)
print("="*len(h))

for angle in range(0 , 361 , 20):
    radian = math.radians(angle)
    print(f"|{angle:4}|",end="")
    print(f"|{math.sin(radian):9.5f}|",end="")
    print(f"|{math.cos(radian):9.5f}|",end="")
    print(f"|{math.tan(radian):9.5f}|")

print("="*len(h))
