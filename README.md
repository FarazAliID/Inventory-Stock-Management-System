# Inventory & Stock Management System 📦

A file-based Python application designed to manage products, track stock levels, and record purchase and sales activities efficiently. Built as a final project for the PITP (People's Information Technology Program).

**Developed by:** Faraz Ali

---

## 📌 Project Description

The Inventory & Stock Management System helps small shops or businesses maintain accurate stock records without using a complex database system. The main purpose of this project is to automate inventory handling, reduce manual errors, and provide real-time stock updates using text and CSV files for storage.

---

## 🎯 Objectives

* Track product stock accurately.
* Manage purchases and sales records.
* Automatically update stock levels.
* Alert the user when stock becomes low.
* Generate clear stock reports.

---

## 🏗️ System Overview

The project is structured modularly across multiple Python files:

* `products.txt`: Stores product details such as ID, name, price, and quantity.
* `transactions.csv`: Records all purchase and sale transactions with quantity.
* `main.py`: Runs the menu-driven CLI interface.

---

## ✨ Functional Features

* ➕ **Add Products:** Register new products with ID, name, category, price, and stock.
* 🔄 **Update Products:** Modify existing product details such as price or stock.
* ❌ **Delete Products:** Remove unused items from the system.
* 📝 **Record Transactions:** Log all purchase and sale activities into CSV files.
* ⚡ **Automatic Stock Update:** Real-time stock adjustment following transactions.
* ⚠️ **Low Stock Alert:** Warning triggers when stock falls below threshold levels.
* 📊 **Stock Reports:** Summary view of current stock status and inventory metrics.

---

## 📸 Main Interface

![Main Menu](https://raw.githubusercontent.com/FarazAliID/Inventory-Stock-Management-System/main/Screenshots/Output-Screenshot/main-menu.jpg)

> 📁 **Note:** All project screenshots are organized in the [`Screenshots/`](https://github.com/FarazAliID/Inventory-Stock-Management-System/tree/main/Screenshots) folder:
> * 💻 [Code Screenshots](https://github.com/FarazAliID/Inventory-Stock-Management-System/tree/main/Screenshots/Code-Screenshots)
> * 📄 [Data Files Screenshots](https://github.com/FarazAliID/Inventory-Stock-Management-System/tree/main/Screenshots/Data-Screenshots)
> * 🖥️ [Output Screenshots](https://github.com/FarazAliID/Inventory-Stock-Management-System/tree/main/Screenshots/Output-Screenshot)

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FarazAliID/Inventory-Stock-Management-System

   cd Inventory-Stock-Management-System

   python main.py
