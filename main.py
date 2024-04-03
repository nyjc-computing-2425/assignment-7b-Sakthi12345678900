# Built-in imports
import math

# Your code below

GRADE = {}

for score in range(101):
    if score >= 70:
        GRADE[score] = 'A'
    elif score >= 60:
        GRADE[score] = 'B'
    elif score >= 55:
        GRADE[score] = 'C'
    elif score >= 50:
        GRADE[score] = 'D'
    elif score >= 45:
        GRADE[score] = 'E'
    elif score >= 40:
        GRADE[score] = 'S'
    else:
        GRADE[score] = 'U'

def read_testscores(filename):
    import csv
    studentdata = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p1 = int(row[2])
            p2 = int(row[3])
            p3 = int(row[4])
            p4 = int(row[5])
            overall = math.ceil((p1 / 30 * 15) + (p2 / 40 * 30) + (p3 / 80 * 35) + (p4 / 30 * 20))
            grade = GRADE[overall]
            studentdata.append({
                'class': row[0],
                'name': row[1],
                'overall': overall,
                'grade': grade
            })
        return studentdata

def analyze_grades(studentdata):
    analysis = {}
    for student in studentdata:
        class_ = student['class']
        grade = student['grade']
        if class_ not in analysis:
            analysis[class_] = {}
        if grade not in analysis[class_]:
            analysis[class_][grade] = 1
        else:
            analysis[class_][grade] += 1
    return analysis 
                
            
            

