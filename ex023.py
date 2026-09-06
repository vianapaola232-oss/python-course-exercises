number = int(input("Type a number: "))
ones = number // 1 % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10
print("Analyzing...")
print(f"""Ones: {ones}
Tens: {tens}
hundreds: {hundreds}
Thousands: {thousands}""")
