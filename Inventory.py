class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to inventory.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                print(f"Product '{product.name}' removed from inventory.")
                return
        print("Product not found in inventory.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return

        print("Inventory:")
        print("ID  |  Name  |  Price  |  Quantity")
        print("-" * 35)
        for product in self.products:
            print(f"{product.id:2}  |  {product.name:5}  |  ${product.price:.2f}  |  {product.quantity:2}")

# Sample usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products to inventory
    inventory.add_product(Product(1, "Laptop", 800, 10))
    inventory.add_product(Product(2, "Phone", 500, 20))
    inventory.add_product(Product(3, "Tablet", 300, 15))

    # Displaying inventory
    inventory.display_inventory()

    # Removing a product from inventory
    inventory.remove_product(2)

    # Displaying inventory after removal
    inventory.display_inventory()
