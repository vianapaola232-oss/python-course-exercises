from math import sin, cos, tan, radians
angle = float(input("Enter an angle: "))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print(f"Analyzing the angle {angle}º, its sine is {sine:.2f}, its cosine is {cosine:.2f} and its tangent is {tangent:.2f}.")
