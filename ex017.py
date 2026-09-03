import math
opposite_leg = float(input("What's the length of the opposite leg: "))
adjacent_leg = float(input("What's the length of the adjacent leg: "))
hypotenuse = math.sqrt((opposite_leg ** 2 ) + (adjacent_leg ** 2))
print(f"The hypotenuse length is {hypotenuse:.2f}.")
