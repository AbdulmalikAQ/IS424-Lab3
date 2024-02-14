employees = dict()

while True:
    emp_name = input("Enter employee's name (enter 'no' to stop): ")
    if emp_name.lower() == "no":
        break
    emp_salary = int(input("Enter employee's salary: "))
    employees[emp_name] = emp_salary
    print("Employee '" + emp_name + "' entered!")

for emp_name, emp_salary in employees.items():
    print(emp_name + ":", emp_salary)