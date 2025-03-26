def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it is 20% or more."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Get user input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied. The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {original_price:.2f}")


