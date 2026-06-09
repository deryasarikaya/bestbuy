import products


class Store:

    def __init__(self, product_list):
        """Initialize the store with a list of Product instances."""
        for item in product_list:
            if not isinstance(item, products.Product):
                raise ValueError("All items in product_list must be Product instances")

        self.products = product_list

    def add_product(self, product):
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Process a shopping list and return the total price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price