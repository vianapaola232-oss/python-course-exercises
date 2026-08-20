rented_days = int(input("How many days was the car rented? "))
km_driven = float(input("How much kilometers were driven? "))
total_rent = (rented_days * 60) + (km_driven * 0.15)
print(f"The total to pay is US${total_rent:.2f}")
