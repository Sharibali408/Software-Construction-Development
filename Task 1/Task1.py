def calculate_billing():
    # Inputs
    product_name = input("Product: ")
    try:
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid input! Please enter numbers for price and quantity.")
        return

    # Calculations
    subtotal = price * quantity
    discount = 0.10 * subtotal  # 10% discount
    final_amount = subtotal - discount

    # Output matching the required format
    print(f"Product: {product_name}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Final Amount: {final_amount}")

# Run the program
calculate_billing()