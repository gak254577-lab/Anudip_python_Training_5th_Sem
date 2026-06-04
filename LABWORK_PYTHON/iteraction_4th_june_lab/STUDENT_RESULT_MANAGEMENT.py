## Problem Statement: Accept marks of 5 subjects. 
# Display: 
# • Total Marks  
# • Percentage  
# • Grade  
# Grade Criteria: 
# Percentage Grade 
# >=90 A+ 
# >=75 A 
# >=60 B 
# >=40 C 
# <40 Fail 
# Also display the number of subjects failed. 




total = 0
failed = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks

    if marks < 40:
        failed += 1

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Failed Subjects:", failed)





## python -u "LABWORK_PYTHON/STUDENT_RESULT_MANAGEMENT.py"