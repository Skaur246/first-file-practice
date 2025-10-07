def calculate_discounted_price(price, discount):
    return price - (price * discount)

# Apply function for each customer
final_price1 = calculate_discounted_price(100, 0.10)
final_price2 = calculate_discounted_price(250, 0.15)
final_price3 = calculate_discounted_price(50, 0.05)

# Print results
print("Customer 1 Final Price:", final_price1)
print("Customer 2 Final Price:", final_price2)
print("Customer 3 Final Price:", final_price3)