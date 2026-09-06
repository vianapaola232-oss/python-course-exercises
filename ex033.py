first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
maximum = first_number
if second_number > third_number and second_number > first_number:
    maximum = second_number
if third_number > first_number and third_number > second_number:
    maximum = third_number
minimum = first_number
if second_number < third_number and second_number < first_number:
    minimum = second_number
if third_number < first_number and third_number < second_number:
    minimum = third_number

print(f"The maximum number is {maximum}.")
print(f"The minimum number is {minimum}.")