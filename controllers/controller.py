from flask import render_template
from app import app
from models.order_list import all_orders

@app.route('/orders')
def index():
    return render_template("index.html", title="Orders", all_orders=all_orders)