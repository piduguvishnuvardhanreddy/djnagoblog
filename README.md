# Blog API (Django REST Framework)

## 🚀 Overview

A RESTful Blog API built using Django and Django REST Framework with JWT authentication and full CRUD functionality.

## ✨ Features

* User authentication using JWT
* Create, Read, Update, Delete blog posts
* User-specific data access (each user sees only their posts)
* Secure API endpoints
* Django admin panel for management

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## 🔐 Authentication

JWT-based authentication using SimpleJWT

## 📡 API Endpoints

### Auth

* POST /api/login/

### Posts

* GET /api/posts/
* POST /api/posts/
* GET /api/posts/{id}/
* PUT /api/posts/{id}/
* DELETE /api/posts/{id}/

## ⚙️ Setup Instructions

```bash
git clone <repo-link>
cd djnagoblog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 👨‍💻 Author

Pidugu Vishnuvardhan Reddy

Your Name
