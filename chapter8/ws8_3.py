def read_scores():
    scores = ()
    done = True
    count = 1
    while done:
        score = int(input(f"Enter score #{count} (-1 to exit) : "))
        if score >= 0 and score <= 100:
            scores += (score,)
            count += 1
        elif score == -1:
            break
    
    count -= 1
    return( scores )

def check_grades(scores):
    grades = ()
    for score in scores:
        grade = ""
        if score >= 80:
            grade = "A"
        elif score >= 80:
            grade = "A"
        elif score >= 80:
            grade = "A"
        elif score >= 80:
            grade = "A"
        else:
            grade = "F"
        grades += (grade,)
    return(grades)

def report_grades(scores,grades):
    Max = len(scores)
    print("="*24)
    print("| No. | Scores | Grade |")
    print("="*24)
    for n in range(Max):
        print(f"| %2d | %3d | %s |" % (n,scores[n],grades[n]))
    print("="*24)

scores = read_scores()
grades  = check_grades(scores)
report_grades(scores,grades)
print(f"End Program.")