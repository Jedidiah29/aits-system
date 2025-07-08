# 🛠️ Academic Issue Tracking System (AITS)

A Django-based backend API to help universities track, respond to, and manage academic-related issues like missing marks, registration errors, or delayed coursework feedback.

## 🔍 Features
- Create and manage student academic issues
- RESTful API built with Django REST Framework
- Admin panel to manage all data
- JSON endpoints for integration with a frontend (React coming soon)

## 🔗 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/api/issues/`      | List all issues          |
| POST   | `/api/issues/`      | Submit new issue         |
| GET    | `/api/issues/<id>/` | Get single issue         |
| PUT    | `/api/issues/<id>/` | Update issue             |
| DELETE | `/api/issues/<id>/` | Delete issue             |

## ⚙️ Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite (default DB for now)

## 📁 Project Structure

aits-system/
├── aits/ ← Django project
├── issues/ ← Issues app
├── manage.py
├── requirements.txt ← [create this if needed]
├── README.md


## ✍️ Author

Jedidiah Allio  
[GitHub](https://github.com/Jedidiah29) 
• [LinkedIn](https://linkedin.com/in/jedidiahallio)
