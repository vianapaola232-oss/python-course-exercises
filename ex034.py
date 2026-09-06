current_salary = float(input("What is the employee's current salary? US$"))
if current_salary <= 1250:
    increase = '15%'
    new_salary = current_salary * 1.15
else:
    increase = '10%'
    new_salary = current_salary * 1.10
print(f"The employee's current salary is US${current_salary:.2f}. After an increase of {increase}, the new salary is US${new_salary:.2f}.")
