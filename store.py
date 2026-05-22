import products


class Store:

    def __init__(self, product_list):
        # Store all products inside the store
        self.products = product_list

    def add_product(self, product):
        # Add a new product to the store
        self.products.append(product)

    def remove_product(self, product):
        # Remove a product from the store
        self.products.remove(product)

    def get_total_quantity(self):
        # Calculate the total quantity of all products
        total_quantity = 0

        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        # Return only active products
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        # Process the shopping list and calculate total price
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


if __name__ == "__main__":

    # Create product objects
    bose = products.Product(
        "Bose QuietComfort Earbuds",
        price=250,
        quantity=500
    )

    mac = products.Product(
        "MacBook Air M2",
        price=1450,
        quantity=100
    )

    # Create store instance with initial products
    best_buy = Store([bose, mac])

    pixel = products.Product(
        "Google Pixel 7",
        price=500,
        quantity=250
    )

    # Add another product to the store
    best_buy.add_product(pixel)

    # Print total quantity in store
    print(best_buy.get_total_quantity())

    # Get all active products
    products_list = best_buy.get_all_products()

    # Make an order and print total price
    print(best_buy.order([
        (products_list[0], 1),
        (products_list[1], 2)
    ]))