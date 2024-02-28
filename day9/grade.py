student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminoe": 99,
    "Draco": 74,
    "neville": 62
}

student_grades = {}

for grade in student_scores:
    
    if 91 <= student_scores[grade] <= 100:  
        student_grades[grade] = "Outstanding"
        
    elif 81 <= student_scores[grade] <= 90:
        student_grades[grade] = "Exceeds Expectations"
        
    elif 71 <= student_scores[grade] <= 80:
        student_grades[grade] = "Acceptable"
    
    else:
        student_grades[grade] = "Fail"
        
print(student_grades)
