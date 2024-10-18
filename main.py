class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []  # User's orders

    def create_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []  # List of products in the order
        self.status = 'Pending'

    def add_product(self, product):
        self.products.append(product)

    def complete_order(self):
        self.status = 'Completed'


class Payment:
    def __init__(self, payment_id, order, amount):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.status = 'Pending'

    def process_payment(self):
        self.status = 'Completed'
        self.order.complete_order()


# Example Usage
if __name__ == "__main__":
    user1 = User(1, "Tanish", "tanish@example.com")
    product1 = Product(101, "Laptop", 1500)
    product2 = Product(102, "Headphones", 200)

    order1 = Order(201, user1)
    order1.add_product(product1)
    order1.add_product(product2)

    payment1 = Payment(301, order1, 1700)
    payment1.process_payment()

    print(f"Order Status: {order1.status}")
    print(f"Payment Status: {payment1.status}")
