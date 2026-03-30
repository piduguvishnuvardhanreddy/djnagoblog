# Blog API (Django REST Framework)

## 🚀 Features

* User Authentication (JWT)
* CRUD operations on Blog Posts
* User-specific data filtering
* Secure API endpoints
* Django Admin Panel

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## 🔐 Authentication

* JWT-based authentication

## 📡 API Endpoints

### Auth

* POST /api/login/

### Posts

* GET /api/posts/
* POST /api/posts/
* GET /api/posts/{id}/
* PUT /api/posts/{id}/
* DELETE /api/posts/{id}/

## ⚙️ Setup

```bash
git clone <your-repo>
cd blog_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 👨‍💻 Author

Your Name
