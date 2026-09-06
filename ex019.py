from random import choice
first = str(input("Name of the first student: ")).strip()
second = str(input("Name of the second student: ")).strip()
third = str(input("Name of the third student: ")).strip()
fourth = str(input("Name of the fourth student: ")).strip()
students = [first, second, third, fourth]
chosen_one = choice(students)
print(f"The chosen student was {chosen_one}.")
