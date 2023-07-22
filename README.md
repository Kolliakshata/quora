# quora
This is a simple Quora website created using Django, where users can post questions, provide answers, and interact with each other's content.

Table of Contents
--------------------
Features
Technologies Used
Setup Instructions
Usage

Features
--------------
User registration and login functionality.
Posting questions and providing answers.
Liking answers posted by others.
Follow topics and receive notifications.
Basic admin interface for managing data.

Technologies Used
--------------------
Django
Django Forms
HTML
CSS (Minimal styling for functionality)
Python

Setup Instructions
---------------------
1.Clone the repository:
git clone <repository_url>
cd quora_project

2.Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate (for Linux/Mac)
venv\Scripts\activate (for Windows)

3.Install the required packages:
pip install -r requirements.txt
Run database migrations:
python manage.py migrate

4.Create a superuser to access the admin interface:
python manage.py createsuperuser

5.Start the development server:
python manage.py runserver
Access the website at http://127.0.0.1:8000/ and the admin interface at http://127.0.0.1:8000/admin/.

Usage
-------
Create a new account or use the superuser account to log in.
Post questions, view questions, and answer questions.
Like answers provided by others.
Follow topics of interest and receive notifications for new content.

