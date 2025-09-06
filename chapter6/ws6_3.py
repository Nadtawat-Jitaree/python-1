total = 0.0
for n in range(1,5):
    point = int(input(f"Enter point grade {n} (0-4) :"))
    total += point

credit = 4
gpa = total / credit
print()
print("You have %d subject"%credit)
print("You have total point =  %5.2f %d , credit"%(total,credit))
print("You get gpa  %5.2f"%gpa)