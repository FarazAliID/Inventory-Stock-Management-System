from inventory import Inventory
from reports import Reports
import os

#====> This Is Colors Code With Variables Easy To Use
Red = '\x1b[1;31m'
Green = '\x1b[1;32m'
Yellow = '\x1b[1;33m'
Blue = '\x1b[1;34m'
MAGENTA = '\x1b[1;35m'
CYAN = '\x1b[1;36m'
WHITE = '\x1b[1;37m'
Rest = '\x1b[0m'

# This Is Clear Screen Function: for terminal
	
def clear():
        os.system("cls")

clear()

#====> Main Function:
def main():
    inv = Inventory()
    while True:
        print('-'*50+ "\n"+ f"{Green}INVENTORY & STOCK MANAGEMENT SYSTEM BY (Faraz Ali){Rest}"+"\n" + '-'*50)
        print("[1] Add Product")
        print("[2] Product Purchase")
        print("[3] Product Sale")
        print("[4] Delete Product")
        print("[5] Stock Report")
        print("[6] Exit Program")
        
        print('-'*50)
        choice = input("Enter Choice: ")
        print('-'*50)
        
        
        if choice == "1":
            p_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            cat = input("Enter Product Category: ")
            price = input("Enter Product Price: ")
            stock = input("Enter Initial Stock: ")
            inv.add_product(p_id, name, cat, price, stock)
            print('-'*50)
            print(f"{Red}Product Added Successful In File{Rest}")
            print('-'*50)
            input("Press Enter To Back Main Menu")
            clear()
            
            
        elif choice == "2":
            p_id = input("Enter Product ID: ")
            qty = int(input("Enter Quantity Purchased: "))
            if inv.update_stock(p_id, qty, "Purchase"):
                print('-'*50 + "\n" + f"{Green}Product Purchased Successful & Stock Updated Successful.{Rest}"+"\n"+'-'*50)
                input("Press Enter To Back Main Menu")
                clear()
            else:
                print("Product Not Found.")
                
        elif choice == "3":
            p_id = input("Enter Product ID: ")
            qty = int(input("Enter Quantity Sold: "))
            if inv.update_stock(p_id, qty, "Sale"):
                print('-'*50 + "\n" + f"{Yellow}Product Saled Successful & Stock Updated Successful.{Rest}"+"\n"+'-'*50)
                input("Press Enter To Back Main Menu")
                clear()
            else:
                print("Product Not Found.")
                
        elif choice == "4":
            p_id = input("Enter Product ID to Delete Product: ")
            inv.delete_product(p_id)
            print('-'*50 + "\n" + f"{Blue}Product Delete Successful From File{Rest}"+"\n"+'-'*50)
            input("Press Enter To Back Main Menu")
            clear()
            
        elif choice == "5":
            Reports.stock_report(inv.products)
        elif choice == "6":
        	break
if __name__ == "__main__":
    main()
