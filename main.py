import products
import store


def show_menu():
    """Display the store menu."""
    print()
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(best_buy):
    """Display all active products in the store."""
    print("------")

    product_list = best_buy.get_all_products()

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.show()}")

    print("------")


def make_order(best_buy):
    """Create an order from user input."""
    shopping_list = []
    product_list = best_buy.get_all_products()

    list_products(best_buy)

    print("When you want to finish order, enter empty text.")

    while True:
        product_number = input("Which product # do you want? ")
        amount = input("What amount do you want? ")

        if product_number == "" or amount == "":
            break

        product_number = int(product_number)
        amount = int(amount)

        product = product_list[product_number - 1]
        shopping_list.append((product, amount))

        print("Product added to list!")
        print()

    try:
        total_price = best_buy.order(shopping_list)

        print("********")
        print(f"Order made! Total payment: ${total_price}")

    except ValueError as error:
        print(f"Order failed: {error}")


def start(best_buy):
    """Run the store menu."""
    while True:
        show_menu()

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(best_buy)

        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    start(best_buy)