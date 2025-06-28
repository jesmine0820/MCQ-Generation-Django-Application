Resource: https://youtu.be/lucFygsnlgM?si=jXvdELAvn5SWS1Cx

1. Create new environment
conda create -p env python-3.12 -y

2. Activate our env
conda activate env/

3. Install Django
pip install Django

4. Create a new Django project
django-admin startproject quiz_project

5. Start a new app
python manage.py startapp quiz_app

6. Migration
python manage.py migrate
