from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Rate Limiter (optional for backend APIs)
limiter = Limiter(get_remote_address, app=app)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        if mongo.db.users.find_one({"email": data['email']}):
            flash("Email already exists.")
            return redirect('/register')

        mongo.db.users.insert_one({
            "username": data['username'],
            "email": data['email'],
            "password": hashed_pw
        })

        flash("Registration successful! Please login.")
        return redirect('/login')
    return render_template("register.html", title="Register")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = mongo.db.users.find_one({"email": data['email']})

        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
            return render_template('profile.html', username=user['username'], email=user['email'])
        else:
            flash("Invalid email or password.")
            return redirect('/login')
    return render_template("login.html", title="Login")

@app.route('/profile')
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)
