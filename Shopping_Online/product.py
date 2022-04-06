class Product:
    def __init__(self, name, description, seller, price, available):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = available

    def __str__(self):
        return f"Product({self.name}, {self.description}) at ${self.price}"