# str.isalpha() สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวอักษะเท่านั้น 
# str.isalnum() สำหรับตรวจสอบสติงว่ามีค่าเป็นตัวเลข และตัวอักษร
# str.isnumeric() สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวเลข
# str.isdecimal() สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวเลข
# str.isdigit() สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวเลข
# str.islower() สำหรับตรวจสอบสตริงว่าเป็นตัวอักษรเล็ก
# str.isupper() สำหรับตรวจสอบสตริงว่าเป็นตัวอักษรใหญ่
# str.istitle() ตรวจสอบสตริงว่ามีลักษณะเป็น title
# str.isspace() ตรวจสอบสตริงว่าเป็นช่องว่าง

s = input("Enter string : ")
print()

print(f"String is alpha = {s.isalpha()}")
print(f"String is alpha and numeric = {s.isalnum()}")
print(f"String is numeric = {s.isnumeric()}")
print(f"String is decimal = {s.isdecimal()}")
print(f"String is digit = {s.isdigit()}")
print(f"String is lower = {s.islower()}")
print(f"String is upper = {s.isupper()}")
print(f"String is space = {s.isspace()}")
print(f"String is title = {s.istitle()}")