salary = float(input("Enter the salary of employee:"))

if salary > 50000:
    print("High Income")
elif salary>=30000 and salary <= 50000:
    print("Medium Income")
elif salary < 30000:
    print("Low Income")
else :
    print("Go to nearest hospital!")