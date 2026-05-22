class Product:

    def __init__(self, name: str, price: float, quantity: int):

        # Validate input values
        if name == "":
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        # Store product data
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # Return current quantity
    def get_quantity(self) -> int:
        return self.quantity

    # Update product quantity
    def set_quantity(self, quantity: int):

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        # Deactivate product if quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

    # Return active status
    def is_active(self) -> bool:
        return self.active

    # Activate product
    def activate(self):
        self.active = True

    # Deactivate product
    def deactivate(self):
        self.active = False

    # Print product information
    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    # Buy a certain amount of the product
    def buy(self, quantity: int) -> float:

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        # Check if enough items are in stock
        if quantity > self.quantity:
            raise ValueError(
                f"Not enough quantity in stock. Available: {self.quantity}"
            )

        # Calculate total purchase price
        total_price = self.price * quantity

        # Reduce stock quantity
        self.set_quantity(self.quantity - quantity)

        return total_price


if __name__ == "__main__":

    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()