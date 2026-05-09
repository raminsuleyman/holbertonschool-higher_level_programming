from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Get all usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Get user by username
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# Add new user
@app.route("/add_user", methods=["POST"])
def add_user():
    # Validate JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create user object
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


# Run server
if __name__ == "__main__":
    app.run()
