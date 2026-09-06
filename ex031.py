distance = float(input("What is the distance of the trip? "))
if distance <= 200:
    cost = distance * 0.5
    print(f"The trip will cost you US${cost:.2f}.")
else:
    cost = distance * 0.45
    print(f"The trip will cost you US${cost:.2f}.")
    