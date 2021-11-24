from flask import render_template
from app import app
from models.order_list import all_orders

@app.route('/orders')
def index():
    return render_template("index.html", title="Orders", all_orders=all_orders)

@app.route("/orders/<index>")
def order(index):
    index_no = int(index)
    order = all_orders[index_no]
    return render_template("order.html", order = order, title = f"Order Details: {order.customer_name}, {order.book_title}")
