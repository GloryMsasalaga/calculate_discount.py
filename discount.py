def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Check if a discount was applied and print the final price accordingly
if final_price != original_price:
    print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
else:
    print("No discount applied. The original price remains unchanged: $", original_price)
