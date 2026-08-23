class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = int(stock)

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Stock: {self.stock}"
