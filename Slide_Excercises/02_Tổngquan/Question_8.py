import json

# Class Product represents a product
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        return Product(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
        )

# Class ProductManager to manage a list of products
class ProductManager:
    def __init__(self):
        self.products = []

    def view_products(self):
        if not self.products:
            print("The product list is empty!")
        else:
            print("Product list:")
            for product in self.products:
                print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product added: {product.name}")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        for product in self.products:
            if product.product_id == product_id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                print(f"Product with ID {product_id} has been updated.")
                return
        print(f"Product with ID {product_id} does not exist!")

    def delete_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product with ID {product_id} has been deleted.")
                return
        print(f"Product with ID {product_id} does not exist!")

    def serialize_to_json(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([product.to_dict() for product in self.products], file, ensure_ascii=False, indent=4)
        print(f"Data has been saved to file {file_path}.")

    def deserialize_from_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.products = [Product.from_dict(item) for item in data]
            print(f"Data has been loaded from file {file_path}.")
        except FileNotFoundError:
            print(f"File {file_path} does not exist!")

# Main program
def main():
    manager = ProductManager()
    while True:
        print("\nChoose an option:")
        print("1. View product list")
        print("2. Add a product")
        print("3. Update a product")
        print("4. Delete a product")
        print("5. Save to JSON file")
        print("6. Load data from JSON file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.view_products()
        elif choice == "2":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, price, quantity)
            manager.add_product(product)
        elif choice == "3":
            product_id = input("Enter product ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            price = input("Enter new price (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            price = float(price) if price else None
            quantity = int(quantity) if quantity else None
            manager.update_product(product_id, name, price, quantity)
        elif choice == "4":
            product_id = input("Enter product ID to delete: ")
            manager.delete_product(product_id)
        elif choice == "5":
            file_path = input("Enter JSON file path to save: ")
            manager.serialize_to_json(file_path)
        elif choice == "6":
            file_path = input("Enter JSON file path to load: ")
            manager.deserialize_from_json(file_path)
        elif choice == "7":
            print("Exiting program!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
