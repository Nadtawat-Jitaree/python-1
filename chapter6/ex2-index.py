name = "Somchai"
print(f"Length of name = {len(name)}")
print(f"name position 0 = {name[0]}")
print(f"name position -1 = {name[-1]}")
print(f"name position 3 = {name[3]}")
print(f"name position -4 = {name[-4]}")

print("="*30)

# str[start:stop]
print(f"name slicing 0:3 = {name[0:3]}")
print(f"name slicing 3:7 = {name[3:7]}")
print(f"name slicing 3: = {name[3:]}")
print(f"name slicing :4 = {name[:4]}")
print(f"name slicing -1:-4 = {name[-1:-4]}")
print(f"name slicing -5:-1 = {name[-5:-1]}")
print(f"name slicing : = {name[:]}")

# 
print("="*30)

# str[start:stop:step]
print(f"name slicing 0: :2 = {name[0: :2]}")
print(f"name slicing 0: :3 = {name[0: :3]}")
print(f"name slicing -7: :2 = {name[-7: :2]}")
print(f"name slicing -7: :4 = {name[-7: :4]}")

print("="*30)
# start stop step
num = len(name)
print(name[:num])
print(name[:num-1])
print(name[:num-2])
print(name[:num-3])
print(name[:num-4])
print(name[:num-5])
print(name[:num-6])
