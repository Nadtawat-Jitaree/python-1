decum = int(input('Enter decimal number : '))
num = decum
binstr = ""
# bit 0
binstr = str(num % 2)
num = num // 2
# bit 1
binstr = str(num % 2) + binstr
num = num // 2
# bit 2
binstr = str(num % 2) + binstr
num = num // 2
# bit 3
binstr = str(num % 2) + binstr
num = num // 2
# bit 4
binstr = str(num % 2) + binstr
num = num // 2
# bit 5
binstr = str(num % 2) + binstr
num = num // 2

print("Decimal number : ", decum)
print("Binary : ", binstr)