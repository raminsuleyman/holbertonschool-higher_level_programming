#!/usr/bin/python3
"""Flask app reading JSON or CSV with filtering."""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Read products from CSV file."""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


@app.route('/products')
def products():
    """Handle product display with source and id filters."""

    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error, products=[])

    # filter by id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if int(p["id"]) == product_id]
        except:
            data = []

        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)