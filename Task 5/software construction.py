class ShoppingCart:
    """A shopping cart that keeps its items and related operations together."""

    def __init__(self):
        # Each cart gets its OWN dict (created per instance, not shared).
        # Structure: {product_name: {"price": float, "quantity": int}}
        self.items = {}

    def add_item(self, product, price, quantity=1):
        """Add a product with its price and quantity.
        If the product is already in the cart, increase its quantity."""
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be >= 0 and quantity must be > 0.")
        if product in self.items:
            self.items[product]["quantity"] += quantity
        else:
            self.items[product] = {"price": price, "quantity": quantity}

    def calculate_total(self):
        """Return the cart total (sum of price * quantity for every item).
        An empty cart returns 0."""
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    # Extension
    def remove_item(self, product):
        """Remove a product from the cart if it exists."""
        self.items.pop(product, None)


if __name__ == "__main__":
    cart1 = ShoppingCart()
    cart1.add_item("Laptop", 1200.00, 1)
    cart1.add_item("Mouse", 25.50, 2)

    cart2 = ShoppingCart()
    cart2.add_item("Notebook", 3.75, 4)
    cart2.add_item("Pen", 1.20, 10)

    print("Cart 1 items:", cart1.items)
    print("Cart 1 total:", cart1.calculate_total())  # 1251.0
    print("Cart 2 items:", cart2.items)
    print("Cart 2 total:", cart2.calculate_total())  # 27.0

    # Independence check: changing cart2 does not affect cart1
    cart2.remove_item("Pen")
    print("Cart 2 total after removing Pen:", cart2.calculate_total())  # 15.0
    print("Cart 1 total (unchanged):", cart1.calculate_total())  # 1251.0