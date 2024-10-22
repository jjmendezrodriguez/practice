from app import app
from app.user import User
from app.database import load_users, save_users
from flask import request, jsonify
from flask_cors import cross_origin

users = load_users()

""" Manejar el usuario registrado,
    registra nuevos usuarios."""
@app.route('/register_user', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    # confirm_password = data.get('confirm_password')

    # if password != confirm_password:
    #     return jsonify({"error": "Passwords do not match"}), 400
    
    if email in users:
        return jsonify({"\nerror": "User already exists\n"}), 400

    user = User(username, email, password)
    users[username] = user.to_dict()
    save_users(users)
    return jsonify(user.to_dict()), 201

# maneja el login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_dict = users.get(username)
    if not user_dict:
        return jsonify({"\nerror": "Invalid credentials\n"}), 401

    user = User(**user_dict)
    if not user.check_password(password):
        return jsonify({"\nerror": "Invalid credentials\n"}), 401

    return jsonify(user.to_dict())

# info del usuario

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user_dict = users.get(username)
    if not user_dict:
        return jsonify({"\nerror": "User not found\n"}), 404

    return jsonify(user_dict)
