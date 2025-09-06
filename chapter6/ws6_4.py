import math
print()
print("="*45)
print("|Angle|    Sin   |    Cos    |   Tan     |")
print("="*45)
for angle in range(0,361,20):
    radian = math.radians(angle)
    print(f"| {angle:4} |",end="")
    print(f"| {math.sin(radian):9.5f} |",end="")
    print(f"| {math.cos(radian):9.5f} |",end="")
    print(f"| {math.tan(radian):9.5f} |")
    print("="*45)

