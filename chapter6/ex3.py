total = 0.0
for n in range(1,5):
    point = int(input(f"Enter point grade {n} (0-4) : "))
    total += point

credit = 4
gpa = total/credit
print()
print(f"You have {credit} subject")
print(f"You have total point = {total:.2f} , {credit} credit")
print(f"You get gpa = {gpa:.2f}")