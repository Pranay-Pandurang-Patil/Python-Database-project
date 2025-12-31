from db import get_connection
from datetime import datetime

def get_all_orders():
    conn = get_connection()
    orders = conn.execute("SELECT * FROM orders").fetchall()
    conn.close()
    return orders

def create_order(customer_name, customer_address, order_items):
    conn = get_connection()
    cursor = conn.cursor()

    total = 0
    for item in order_items:
        total += item["price"] * item["quantity"]

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute(
        "INSERT INTO orders (customer_name, customer_address, order_date, total_amount) VALUES (?, ?, ?, ?)",
        (customer_name, customer_address, date, total)
    )
    order_id = cursor.lastrowid

    for item in order_items:
        cursor.execute(
            "INSERT INTO order_details (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, item["product_id"], item["quantity"])
        )

    conn.commit()
    conn.close()


def get_order_details(order_id):
    conn = get_connection()
    details = conn.execute("""
        SELECT p.name, p.price, p.unit, od.quantity
        FROM order_details od
        JOIN products p ON od.product_id = p.product_id
        WHERE od.order_id = ?
    """, (order_id,)).fetchall()
    conn.close()
    return details

def get_order(order_id):
    conn = get_connection()
    order = conn.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,)).fetchone()
    conn.close()
    return order
