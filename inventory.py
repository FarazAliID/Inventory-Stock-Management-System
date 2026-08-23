from file_handler import FileHandler
from product import Product

class Inventory:
    def __init__(self):
        self.fh = FileHandler()
        self.products = self.fh.load_products()

    def add_product(self, p_id, name, category, price, stock):
        product = Product(p_id, name, category, price, stock)
        self.products.append(product)
        self.fh.save_products(self.products)

    def update_stock(self, p_id, quantity, t_type):
        for p in self.products:
            if p.product_id == p_id:
                if t_type == "Purchase":
                    p.stock += quantity
                elif t_type == "Sale":
                    p.stock -= quantity
                self.fh.save_products(self.products)
                # Matches user requested CSV columns: Product id, Type sale purchase, quantity
                self.fh.save_transaction([p_id, t_type, quantity])
                return True
        return False

    def delete_product(self, p_id):
        self.products = [p for p in self.products if p.product_id != p_id]
        self.fh.save_products(self.products)
