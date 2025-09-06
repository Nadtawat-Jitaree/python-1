# Workshop 8_1

def Check_Point(grade):
    point = 0
    if grade == 'A': point = 4
    elif grade == "B": point = 3
    elif grade == "C": point = 1
    elif grade == "D": point = 2
    elif grade == "F": point = 0 
    return (point)

Done = True
while Done:
    grade = input("Enter grade (Q-exit) : ")
    grade = grade.upper()
    if grade == "Q":
        Done = False
    else:
        value = Check_Point( grade)
        print(f"Point Value of {grade} is {value}")

print("End Program.")