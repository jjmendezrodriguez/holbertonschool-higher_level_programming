#!/usr/bin/python3

from flask import abort
from flask import Flask, jsonify, request

# Instantiate a Flask web server from the Flask module
app = Flask(__name__)

# In-memory dictionary to store user data
users = {}


# Define a route for the root URL ("/") and create a function to handle this route
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Create a new route /data to return a list of all usernames stored in the API
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


# Add a route to return OK status
@app.route('/status')
def get_status():
    return "OK"

# Add a dynamic route to get user information by username
@app.route('/users/<username>')
def get_user(username):
    # specified
        if username not in users:
            return jsonify({"error": "User not found"}), 404
        
        outputs = users[username]
        outputs["username"] = username

        return jsonify(outputs)

# Add a route to handle POST requests to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.get_json() is None:
        abort(400, "not a json")

    req_data = request.get_json()
    
    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400
    
    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    

    outputs = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]        
    }
    return jsonify({"message": "User added", "user": outputs}), 201

# Run the Flask development server
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
