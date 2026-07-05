import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def get_items():
    json_path = 'items.json'

    if not os.path.exists(json_path):
        return render_template('items.html', items=[])

    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (json.JSONDecodeError, IOError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True)
