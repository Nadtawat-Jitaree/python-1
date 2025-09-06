import sys # import sys เพื่อใช้ getsizeof ตรวจสอบขนาดของหน่วยความจำที่ใช้ไป
S1 = "Python"
S2 = "Hello World"
Salary = 15890.00
Age = 34

print("Str Python",sys.getsizeof(S1))
print("Hello World",sys.getsizeof(S2))
print("Salary",sys.getsizeof(Salary))
print("Age",sys.getsizeof(Age))
