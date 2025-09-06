# Workshop 8_1

def Check_Point(grade):
    grades = ('A','B','C','D','F')
    values = (4,3,2,1,0)
    for n in range(len(grades)):
        if grade == grades[n]:
            return(values[n])

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