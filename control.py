def calculate_discount(price, discount_percent):
    """Return the final price after applying discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # No discount applied
    
# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display results
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {final_price:.2f}")
