
from db import create_tables
from products import add_product, get_all_products, delete_product, get_product, update_product
from orders import get_all_orders, create_order, get_order_details

import os
from flask import Flask, render_template, request, redirect

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

create_tables()

@app.route("/")
def index():
    orders = get_all_orders()
    return render_template("index.html", orders=orders)

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        add_product(
            request.form["name"],
            request.form["price"],
            request.form["unit"]
        )
        return redirect("/products?success=product_added")

    products = get_all_products()
    return render_template("products.html", products=products)

@app.route("/new_order", methods=["GET", "POST"])
def new_order():
    products = get_all_products()

    if request.method == "POST":
        customer_name = request.form["customer_name"]
        customer_address = request.form["customer_address"]

        items = []
        for p in products:
            qty = request.form.get(f"qty_{p['product_id']}")
            if qty and float(qty) > 0:
                items.append({
                    "product_id": p["product_id"],
                    "price": p["price"],
                    "quantity": float(qty)
                })
        
        create_order(customer_name, customer_address, items)
        return redirect("/?success=new_order")



    return render_template("new_order.html", products=products)

@app.route("/order/<int:order_id>")
def order_details(order_id):
    from orders import get_order # importing here to avoid circular if any, or just easy add
    details = get_order_details(order_id)
    order = get_order(order_id)
    return render_template("order_details.html", details=details, order=order)

@app.route("/delete_product/<int:product_id>")
def remove_product(product_id):
    delete_product(product_id)
    return redirect("/products")

@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    if request.method == "POST":
        update_product(
            product_id,
            request.form["name"],
            request.form["price"],
            request.form["unit"]
        )
        return redirect("/products")

    product = get_product(product_id)
    return render_template("edit_product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)