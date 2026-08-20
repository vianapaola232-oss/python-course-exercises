current_salary = float(input("What is the employee's current salary? US$"))
increase = 15 / 100
new_salary = current_salary + (current_salary * increase) # Apply a 15% increase
print(f"The employee's salary after a 15% increase is US${new_salary:.2f}.")