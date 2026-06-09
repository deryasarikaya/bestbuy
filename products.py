class Product:

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with name, price and quantity."""
        if name == "":
            raise ValueError("Name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update product quantity. Deactivates product if quantity reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, requested_quantity: int) -> float:
        """Buy a certain amount of the product and return the total price."""
        if not self.active:
            raise ValueError("Product is not active")

        if requested_quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if requested_quantity > self.quantity:
            raise ValueError(
                f"Not enough quantity in stock. Available: {self.quantity}"
            )

        total_price = self.price * requested_quantity
        self.set_quantity(self.quantity - requested_quantity)

        return total_price