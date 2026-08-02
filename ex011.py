# Wall painting calculator
width = float(input("Enter the wall width in meters (m): "))
height = float(input("Enter the wall height in meters (m): "))

area = width * height
paint_to_cover = area / 1.8

print(f"The wall dimensions are {width:g} m × {height:g} m, for a total area of {area:g} m².")
print(f"To cover this wall, you'll need {paint_to_cover:g} L of paint.")
