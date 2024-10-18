class Inventory:
    def __init__(self):
        self.stock = {}  # Dictionary to store product stock levels (product_id -> quantity)

    def process_orders(self, orders):
        for product_id, quantity in orders.items():
            if product_id in self.stock and self.stock[product_id] >= quantity:
                self.stock[product_id] -= quantity
                print(f"Processed order for Product {product_id}, new stock: {self.stock[product_id]}")
                if self.stock[product_id] < 10:
                    print(f"Product {product_id} stock is low. Please restock.")
            else:
                print(f"Error: Product {product_id} is out of stock or insufficient stock.")

    def restock_items(self, restock_list):
        for product_id, quantity in restock_list.items():
            if product_id in self.stock:
                self.stock[product_id] += quantity
            else:
                self.stock[product_id] = quantity
            print(f"Restocked Product {product_id}, new stock: {self.stock[product_id]}")


# Example Usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.stock = {1: 50, 2: 30, 3: 5}  # product_id -> stock

    # Process orders
    orders = {1: 5, 2: 10, 3: 3}
    inventory.process_orders(orders)

    # Restock low stock items
    restock_list = {3: 20}
    inventory.restock_items(restock_list)
