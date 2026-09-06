from datetime import date
year = int(input("What year would you like to check? (Enter 0 to check the current year):  "))
if year == 0:
    year = date.today().year
if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"\033[31mThe year {year} is not a leap year.\033[m")
