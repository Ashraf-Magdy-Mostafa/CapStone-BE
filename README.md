# 🛒 E-commerce Backend API

> A RESTful backend API for an e-commerce platform, built as part of the
> ALX Capstone Project. The API provides user authentication, product
> management, cart functionality, and order processing.

---

## 📌 Features

- User registration and authentication (JWT)
- Role-based access (admin / user)
- CRUD operations for products
- Shopping cart functionality
- Order creation and order history
- Input validation and error handling

---

## 🛠️ Tech Stack

- Node.js
- Express.js
- MongoDB (or your DB)
- JWT Authentication

---

## 📂 Project Structure

src/ ├── controllers/ ├── routes/ ├── models/ ├── middlewares/ ├──
config/ ├── app.js └── server.js

---

## ⚙️ Getting Started

### 1. Clone the repository

git clone https://github.com/your-username/ecommerce-backend.git

### 2. Install dependencies

cd ecommerce-backend npm install

### 3. Create environment variables

Create a `.env` file:

PORT=5000\
DATABASE_URL=your_database_connection_string\
JWT_SECRET=your_secret_key

### 4. Start the server

npm run dev

Server runs at: http://localhost:5000

---

## 🔐 Sample API Endpoints

Auth: - POST /api/auth/register - POST /api/auth/login

Products: - GET /api/products - POST /api/products (admin)

Orders: - POST /api/orders - GET /api/orders/my

---

## 🧪 Testing

- Tested using Postman
- Verified protected routes and validation

---

## 📄 License

Educational project for ALX Capstone.
