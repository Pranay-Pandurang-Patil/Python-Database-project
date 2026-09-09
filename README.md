# 🛒 Grocery Store Management System

A simple **Grocery Store Management System** built using **Python, Flask, SQLite, HTML, CSS, and JavaScript**.

The application provides a web-based interface for managing grocery products and customer orders. It demonstrates practical implementation of **database connectivity, CRUD operations, relational database design, and Flask web development**.

---

## 📌 Project Overview

The **Grocery Store Management System** is a lightweight web application designed to manage products and customer orders in a grocery store.

The application allows users to:

- Manage grocery products
- Add new products
- View available products
- Edit product information
- Delete products
- Create customer orders
- Add multiple products to an order
- Calculate order totals automatically
- Store customer information
- View complete order details
- Persist data using SQLite

---

## ✨ Features

### 📦 Product Management

- Add new grocery products
- View all products
- Edit existing products
- Delete products
- Store product name
- Store product price
- Store product unit

### 🛍️ Order Management

- Create customer orders
- Enter customer name
- Enter customer address
- Select multiple products
- Specify product quantities
- Automatically calculate order total
- Store order date and time
- View all orders
- View individual order details

### 🗄️ Database

- SQLite relational database
- Automatic database initialization
- Product table
- Orders table
- Order details table
- Primary keys
- Foreign keys
- Relational database structure
- Persistent data storage

### 🌐 Web Interface

- Flask-based web application
- Jinja2 templates
- HTML5
- CSS3
- JavaScript
- Simple and responsive interface

---

## 🛠️ Tech Stack

### Backend

- Python
- Flask

### Database

- SQLite
- Python `sqlite3`

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2

### Tools

- Git
- GitHub
- Python Virtual Environment

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
HTML / CSS / JavaScript
 │
 ▼
Flask Application
 │
 ├── Product Management
 │
 └── Order Management
 │
 ▼
Database Layer
 │
 ▼
SQLite Database
```

---

## 📂 Project Structure

```text
Python-Database-project/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── products.py
│   └── orders.py
│
├── database/
│   └── grocery_store.db
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── products.html
│   ├── edit_product.html
│   ├── new_order.html
│   └── order_details.html
│
└── README.md
```

---

## 🗄️ Database Design

The project uses **SQLite** as its relational database.

### Database

```text
grocery_store.db
```

### Main Tables

```text
products
orders
order_details
```

### Products Table

Stores information about grocery products.

| Column | Type | Description |
|---|---|---|
| product_id | INTEGER | Primary key |
| name | TEXT | Product name |
| price | REAL | Product price |
| unit | TEXT | Product unit |

### Orders Table

Stores customer order information.

| Column | Type | Description |
|---|---|---|
| order_id | INTEGER | Primary key |
| customer_name | TEXT | Customer name |
| customer_address | TEXT | Customer address |
| order_date | TEXT | Order date and time |
| total_amount | REAL | Total order amount |

### Order Details Table

Connects products with orders.

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| order_id | INTEGER | Foreign key |
| product_id | INTEGER | Foreign key |
| quantity | REAL | Ordered quantity |

---

## 🔗 Database Relationship

```text
┌──────────────┐
│   products   │
├──────────────┤
│ product_id PK│
│ name         │
│ price        │
│ unit         │
└──────┬───────┘
       │
       │
       ▼
┌─────────────────┐
│  order_details  │
├─────────────────┤
│ id PK           │
│ order_id FK     │
│ product_id FK   │
│ quantity        │
└────────┬────────┘
         │
         ▼
┌────────────────┐
│     orders     │
├────────────────┤
│ order_id PK    │
│ customer_name  │
│ customer_address│
│ order_date     │
│ total_amount   │
└────────────────┘
```

---

## 🔄 CRUD Operations

The project demonstrates the four fundamental database operations.

### Create

- Add products
- Create customer orders
- Add order details

### Read

- View products
- View orders
- View order details

### Update

- Edit product name
- Edit product price
- Edit product unit

### Delete

- Delete products

---

## ⚙️ How It Works

### Product Management

```text
Add Product
     ↓
Store in SQLite
     ↓
View Products
     ↓
Edit / Delete
```

### Order Creation

```text
Customer Information
        ↓
Select Products
        ↓
Enter Quantities
        ↓
Calculate Total
        ↓
Store Order
        ↓
Store Order Details
```

### Order Total

For each product:

```text
Product Total = Price × Quantity
```

For multiple products:

```text
Order Total =
Product 1 Total
+ Product 2 Total
+ Product 3 Total
+ ...
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Git
- Web browser

SQLite is included with Python through the `sqlite3` module.

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Pranay-Pandurang-Patil/Python-Database-project.git
```

```bash
cd Python-Database-project
```

---

## 🐍 Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

---

## 📦 Install Flask

```bash
pip install flask
```

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Navigate to the backend directory:

```bash
cd backend
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 🖥️ Application Pages

## 🏠 Dashboard

The dashboard provides access to the main functionality of the application and displays customer orders.

---

## 📦 Products

The Products page allows users to:

- Add products
- View products
- Edit products
- Delete products

Product information includes:

```text
Product Name
Price
Unit
```

---

## 🛒 New Order

The New Order page allows users to:

- Enter customer information
- Select products
- Enter quantities
- Create an order
- Automatically calculate the total amount

---

## 📋 Order Details

The Order Details page displays:

- Order ID
- Customer name
- Customer address
- Order date
- Ordered products
- Product prices
- Quantities
- Total amount

---

# 🔐 Database Safety

The application uses parameterized SQL queries when working with user-provided values.

Example:

```python
conn.execute(
    "SELECT * FROM products WHERE product_id = ?",
    (product_id,)
)
```

Parameterized queries help reduce the risk of SQL injection.

---

# 📚 Learning Objectives

This project demonstrates practical understanding of:

- Python programming
- Flask
- SQLite
- SQL
- CRUD operations
- Relational databases
- Primary keys
- Foreign keys
- Database relationships
- Database connectivity
- HTML
- CSS
- JavaScript
- Jinja2 templates
- Form handling
- Backend development
- Frontend integration
- Data persistence

---

# 🧠 Concepts Demonstrated

```text
Python
 │
 ├── Functions
 ├── Modules
 ├── Database Connectivity
 │
 ▼
Flask
 │
 ├── Routes
 ├── Request Handling
 ├── Templates
 └── Forms
 │
 ▼
SQLite
 │
 ├── Tables
 ├── SQL Queries
 ├── Primary Keys
 ├── Foreign Keys
 └── Relationships
```

---

# 🔮 Future Improvements

Possible future improvements:

- User authentication
- Admin dashboard
- Product search
- Product categories
- Inventory management
- Stock tracking
- Low-stock alerts
- Customer management
- Order status tracking
- Sales reports
- Revenue analytics
- Date-based filtering
- Pagination
- REST API
- Improved validation
- Improved error handling
- Responsive UI improvements
- Cloud deployment
- PostgreSQL/MySQL support

---

# 🎯 Project Goals

The main goals of this project are:

- Learn Python database programming
- Understand SQLite
- Practice SQL queries
- Implement CRUD operations
- Understand relational database design
- Build a database-driven Flask application
- Connect frontend and backend
- Practice structured project organization

---

# 👨‍💻 Author

**Pranay Pandurang Patil**

Computer Science & Engineering Student

GitHub:

https://github.com/Pranay-Pandurang-Patil

---

# 📄 License

This project is created for educational and personal learning purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📌 Repository

https://github.com/Pranay-Pandurang-Patil/Python-Database-project
