# 📝 Quiz Project – Django

A web-based quiz project developed using **Python and Django**. This project serves as a learning exercise to explore Django web development, project structure, application creation, and database migration.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Django | Web development framework |
| Conda | Python environment management |
| SQL / SQLite | Database management (Django's default database configuration) |

## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### 1. Create a Conda Environment

```bash
conda create -p ./env python=3.12 -y
```

### 2. Activate the Environment

```bash
conda activate ./env
```

### 3. Install Django

```bash
pip install Django
```

### 4. Create a New Django Project

```bash
django-admin startproject quiz_project
```

### 5. Navigate into the Project Directory

```bash
cd quiz_project
```

### 6. Create a New Django Application

```bash
python manage.py startapp quiz_app
```

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 📂 Project Structure

```text
project-folder/
│
├── env/
│
└── quiz_project/
    │
    ├── manage.py
    │
    ├── quiz_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── quiz_app/
        ├── migrations/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        └── views.py
```

## 📚 Key Django Concepts

| Concept | Description |
|---|---|
| Django Project | The main configuration and structure of the website. |
| Django App | An individual application that provides specific functionality within a Django project. |
| `settings.py` | Stores project configuration and installed applications. |
| `urls.py` | Defines URL patterns and routes requests to the appropriate views. |
| `models.py` | Defines the data models used by the application. |
| `views.py` | Handles application logic and generates responses to user requests. |
| Migrations | Manage changes to database schemas based on Django models. |

## 🔗 Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial – YouTube](https://youtu.be/lucFygsnlgM?si=jXvdELAvn5SWS1Cx)
