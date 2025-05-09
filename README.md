# Employer Management System

A simple Employer Management System API using Django REST Framework with custom authentication.


## Features

- Custom user authentication with email/password
- JWT token-based authentication
- CRUD operations for Employers
- User can only access their employers


## Requirements 

- Python 
- Django 
- Django REST Framework 
- djangorestframework-simplejwt


## Setup

1. Clone the repository
2. Create and activate a virtual environment
	python -m venv ems_venv
	ems_venv\Scripts\activate
3. Navigate to the project directory
	cd ems_project
4. Install dependencies
   	pip install -r requirements.txt
5. Make migrations
	python manage.py makemigrations
	python manage.py migrate
6. Create a superuser
	python manage.py createsuperuser
7. Run the development server
	python manage.py runserver


The API will be accessible at http://127.0.0.1:8000/api/
