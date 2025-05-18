# 🛒 MiniMart - Python OOP E-Commerce System

A command-line e-commerce simulation built with Python's Object-Oriented Programming (OOP) principles. This project showcases a working retail system with customer management, shopping cart functionality, stock control, and admin utilities — all through a simple terminal interface.

---

## 📦 Features

### 👤 Customer
- Register new customers dynamically
- Login with customer ID
- Add/remove products from cart
- View cart contents
- Checkout with total price calculation

### 🛠️ Admin Tools
- Restock products
- View full product catalog
- Low stock alert system
- Generate low stock report

### 📊 Inventory Management
- Tracks and validates stock levels in real-time
- Prevents adding more items to cart than available
- Automatically alerts when stock falls below threshold

---

## 🧱 Technologies Used

- **Language:** Python 3.x
- **Concepts:** OOP (Classes, Encapsulation), CLI Menus, Dictionaries, Lists

---

## 📁 Project Structure

- `Product` class – Handles individual item data and stock updates  
- `Cart` class – Manages cart items, totals, and operations  
- `Customer` class – Links each customer to a personal cart  
- CLI interface – Simulates user interactions with menu-based navigation  
