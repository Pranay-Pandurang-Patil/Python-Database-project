from db import get_connection

def add_product(name, price, unit):
    conn = get_connection()
    conn.execute(
        "INSERT INTO products (name, price, unit) VALUES (?, ?, ?)",
        (name, price, unit)
    )
    conn.commit()
    conn.close()

def get_all_products():
    conn = get_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return products

def delete_product(product_id):
    conn = get_connection()
    conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()

def get_product(product_id):
    conn = get_connection()
    product = conn.execute(
        "SELECT * FROM products WHERE product_id = ?", (product_id,)
    ).fetchone()
    conn.close()
    return product

def update_product(product_id, name, price, unit):
    conn = get_connection()
    conn.execute("""
        UPDATE products
        SET name = ?, price = ?, unit = ?
        WHERE product_id = ?
    """, (name, price, unit, product_id))
    conn.commit()
    conn.close()
