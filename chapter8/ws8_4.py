def check_grade(grade):
    grades = ["A","B+","B","C+","C","D+","D","F"]
    values = [4,3.5,3,2.5,2,1.5,1.0]
    for n in range(len(grades)):
        if grade == grades[n]:
            return(values[n])

done = True
while done:
    grade = input("Enter grade (Q-exit) : ").upper()
    if grade == "Q":
        break   
    else:
        value = check_grade(grade)
        print(f"Score value of {grade} is {value}")

print("End Program.")