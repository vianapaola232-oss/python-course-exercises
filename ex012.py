product_price = float(input("What is the price of the product? US$"))
discount = product_price * (5 / 100)
new_price = product_price - discount
print(f"The price of the product after the discount is US${new_price:.2f}.")
