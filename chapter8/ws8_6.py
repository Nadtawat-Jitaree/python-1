from random import randint

def read_scores(num):
    scores = []
    for n in range(num):
        scores.append(randint(40,100))
    return(scores)

def check_grades(scores):
    SCORES = [80,70,60,50,0]
    GRADES = ["A","B","C","D","F"]
    grades = []
    for score in scores:
        for n in range(len(SCORES)):
            if score >= SCORES[n]:
                grades.append(GRADES[n])
                break
    return(grades)

def report_grades(scores,grades):
    Max = len(scores)
    print("="*24)
    print("| No. | Scores | Grade |")
    print("="*24)
    for n in range(Max):
        print(f"| {n+1} |   {scores[n]}    | {grades[n]}  |")
    print("="*24)
    
num = int(input("Enter number student : "))
scores = read_scores(num)
grades = check_grades(scores)
report_grades(scores,grades)
print("End Program.")