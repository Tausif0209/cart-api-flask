# 🛒 Cart Management System (Flask + MySQL)

A full-stack cart management application built using **Flask (Python)** and **MySQL**, supporting complete CRUD operations with a clean and user-friendly interface.

---

## 🚀 Features

* ➕ Add items to cart
* 📋 View all cart items
* ✏️ Update item details
* ❌ Remove items from cart
* 💰 Calculate total cart price
* 🎨 Simple and responsive UI
* ⚡ RESTful API design

---

## 🏗️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** MySQL
* **Frontend:** HTML, CSS, JavaScript


---

## 📁 Project Structure

```
cart_api/
│
├── app/
│   ├── routes/          # API routes (Blueprints)
│   ├── services/        # Business logic
│   ├── static/          # CSS files
│   ├── templates/       # HTML pages
│   ├── __init__.py      # App factory
│   ├── db.py            # Database connection
│   ├── config.py        # Configurations
│
├── tests/               # Integration tests
├── run.py               # Entry point
├── requirements.txt     # Dependencies
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/Tausif0209/cart-api-flask.git
cd cart-api-flask
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

Run the following SQL:

```sql
CREATE DATABASE cart_db;

USE cart_db;

CREATE TABLE cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    price FLOAT,
    quantity INT
);
```

---

### 4️⃣ Configure Database

Update your `config.py` with your MySQL credentials:

```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'cart_db'
```

---

### 5️⃣ Run the application

```
python run.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---



## 📌 API Endpoints

| Method | Endpoint          | Description     |
| ------ | ----------------- | --------------- |
| POST   | /cart/add         | Add item        |
| GET    | /cart             | View cart items |
| PUT    | /cart/update/<id> | Update item     |
| DELETE | /cart/remove/<id> | Delete item     |
| GET    | /cart/total       | Get total price |

---

## 🎯 Key Concepts Used

* Flask Application Factory Pattern
* Blueprint Routing
* Service Layer Architecture
* MySQL Integration
* Exception Handling
* REST API Design


---



## 👨‍💻 Author

**Tausif Iqbal**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
