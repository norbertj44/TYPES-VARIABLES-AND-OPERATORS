
product_price = float(input("Enter price: "))
discounted_product_price = float(input("Enter discount %: "))

discount_amount = product_price * discounted_product_price / 100
discounted_price = product_price - discount_amount

print(f"Price with discount: {discounted_price:}")
print(f"Reduction: {discount_amount}")
