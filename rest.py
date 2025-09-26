from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to User Management API"}), 200

# Create User (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify(users[user_id]), 201

# Get All Users (GET)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# Get Single User (GET)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Update User (PUT)
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

# Delete User (DELETE)
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)