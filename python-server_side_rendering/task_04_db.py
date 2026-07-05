#!/usr/bin/python3
"""Flask app with JSON, CSV, and SQLite support."""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ---------- JSON ----------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


# ---------- CSV ----------
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


# ---------- SQLITE ----------
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })

        return products

    except Exception:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    # ---------- SOURCE HANDLING ----------
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

    else:
        error = "Wrong source"
        return render_template('product_display.html', products=[], error=error)

    # ---------- FILTER BY ID ----------
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