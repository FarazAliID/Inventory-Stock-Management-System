import csv
import os
from product import Product

class FileHandler:
    def __init__(self):
        self.products_file = "data/products.txt"
        self.transactions_file = "data/transactions.csv"

    def save_products(self, products):
        with open(self.products_file, "w") as file:
            # Added header for .txt file
            file.write("pid,pname,pcategory,pprice,stock\n")
            for p in products:
                file.write(f"{p.product_id},{p.name},{p.category},{p.price},{p.stock}\n")

    def load_products(self):
        products = []
        if os.path.exists(self.products_file):
            with open(self.products_file, "r") as file:
                lines = file.readlines()
                # Skip header line
                if len(lines) > 1:
                    for line in lines[1:]:
                        parts = line.strip().split(",")
                        if len(parts) == 5:
                            products.append(Product(parts[0], parts[1], parts[2], parts[3], parts[4]))
        return products

    def save_transaction(self, transaction):
        file_path = self.transactions_file
        
        # Determine if we need to write the header
        write_header = False
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            write_header = True

        # Open file in append mode
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            
            # Write header if needed
            if write_header:
                writer.writerow(["Pid", "Type", "quantity"])
            
            # Write the transaction
            writer.writerow(transaction)