from random import shuffle
first = str(input("Name of the first student: ")).strip()
second = str(input("Name of the second student: ")).strip()
third = str(input("Name of the third student: ")).strip()
fourth = str(input("Name of the fourth student: ")).strip()
students = [first, second, third, fourth]
shuffle(students)
print(f"The presentation order of the students is {students}.")
