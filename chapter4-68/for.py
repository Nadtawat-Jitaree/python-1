# 6806021610182 ณัฐวัตร จิตอารี
# for

# for ตัวแปร in range(stop) # จะได้ค่า 0 ถึง -1
# ex_1
# print("(n1 ex_1) ============================")
# for n in range(5):
#     print("n1 ex_1",n)


# # ex_2
# print("(n1 ex_2) ============================")
# R = range(5)
# for n in R:
#     print("n1 ex_2",n)

# # for ตัวแปร in range(start,stop) # จะได้ค่า start ถึง stop-1
# print("(n2 ex_1) ============================")
# for n in range(1,6):
#     print("n2",n)

# # for ตัวแปร in range(start,stop,step) # จะได้ค่า start ถึง stop-1 เลื่อค่าที่ละ step
# print("(n3 ex_1) ============================")
# for n in range(10,20,2):
#     print("n3",n)

# # for str
# print("(for str) ============================")
# # ex_1
# print("(ex_1) ============================")
# S =  "Python"
# for c in S:
#     print(c)

# # ex_2
# print("(ex_2) ============================")
# Num = "12345"
# Sum = 0
# for n in Num:
#     Sum += int(n)
#     print(Sum)

data = ('a','b','c','d')
for n in data:
    print("data is ", n)