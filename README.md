# secure_login_flask



# 🔐 Secure Login System with Flask + MongoDB

A secure and user-friendly login system built using **Python Flask** with **MongoDB**, supporting password hashing, rate limiting, and a Bootstrap-powered frontend.

---

## 🚀 Features

- 🧾 User registration & login
- 🔒 Passwords hashed using `bcrypt`
- 📦 MongoDB integration using `Flask-PyMongo`
- 📉 Rate limiting with `Flask-Limiter`
- 🎨 Clean frontend using HTML + Bootstrap
- ⚠️ Flash messages for validation feedback

---

## 🛠️ Tech Stack

| Category     | Tech                          |
|--------------|-------------------------------|
| Backend      | Python, Flask, Flask-PyMongo  |
| Database     | MongoDB (local with Compass)  |
| Frontend     | HTML, Bootstrap               |
| Security     | bcrypt, Flask-Limiter         |
| Dev Tools    | VS Code, Postman              |

---

## 📁 Folder Structure

secure_login_flask/
│
├── app.py # Main Flask app
├── .env # Environment variables (Mongo URI)
├── requirements.txt # Python dependencies
└── templates/ # Frontend HTML (Jinja2)
├── layout.html
├── login.html
├── register.html
└── profile.html




---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/secure_login_flask.git
cd secure_login_flask






**
 Create Virtual Environment (optional but recommended)**
bash

python -m venv venv
venv\Scripts\activate   # On Windows


**Install Dependencies**
bash

pip install -r requirements.txt

** Configure .env File**
**Create a .env file in root directory:**

MONGO_URI=mongodb://localhost:27017/secureLoginDB


**Running the App**
bash

python app.py

Then open your browser and go to:
**http://127.0.0.1:5000**

