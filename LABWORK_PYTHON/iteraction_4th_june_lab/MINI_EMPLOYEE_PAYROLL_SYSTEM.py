name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

if net > 50000:
    grade = "Senior Grade"
elif net > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

print("\nEmployee Name:", name)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Grade:", grade)



## python -u "LABWORK_PYTHON/interaction_4th_june_lab/MINI_EMPLOYEE_PAYROLL_SYSTEM.py"