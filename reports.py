import os

""" Colors """
Magneta = '\x1b[1;35m'
Cyan = '\x1b[1;36m'
Rest = '\x1b[0m'

class Reports:
    def stock_report(products):
        print("--- STOCK REPORT ---")
        for p in products:
            status = "In Stock"
            if p.stock < 10:
                status = "Low Stock Warning"
            print(f"{Magneta}Product: {p.name}")
            print(f"Stock Available: {p.stock}")
            print(f"Status: {status}{Rest}")
            print("-" * 20)
        input("Press Enter To Back Main Menu")
        os.system("cls")
