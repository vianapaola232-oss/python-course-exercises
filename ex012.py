product = float(input("What is the price of the product? US$"))
discount = product * (5 / 100)
new_price = product - discount
print(f"The price of the product after the discount is US${new_price:.2f}.")
