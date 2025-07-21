binnum = int(input('Enter binary number number : '))
num = binnum
# case 2
# bit 0
dec = (num % 10)*1
num = num // 10

# bit 1
dec += (num % 10)*2
num = num // 10

# bit 2
dec += (num % 10)*4
num = num // 10

# bit 3
dec += (num % 10)*8
num = num // 10

# case 1
# # bit 3
# dec = (num // 1000) * 8
# num = num % 1000

# # bit 2
# dec += (num // 100) * 4
# num = num % 100

# # bit 1
# dec += (num // 10) * 2

# # bit 0
# num = num % 10
# dec += num * 1

print("Binary number : ", binnum)
print("Decimal number : ", dec)