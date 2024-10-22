from uuid import uuid4
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import json
from flask import Flask, render_template



app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
CORS(app) # Enable CORS for all routes

with open('data/data.json') as f:
    users = json.load(f)

# In-memory storage for new reviews
new_reviews = []

# for use file html
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# @app.route('/register_user', methods=['POST'])
# def register_user():
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')
#     # confirm_password = data.get('confirm_password')

#     # if password != confirm_password:
#     #     return jsonify({"error": "Passwords do not match"}), 400
    
#     if email in users:
#         return jsonify({"\nerror": "User already exists\n"}), 400

#     user = User(username, email, password)
#     users[username] = user.dict()
#     save_users(users)
#     return jsonify(user.dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
