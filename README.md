# python-login-system
Project developed in python using [**flask framework**](https://flask.palletsprojects.com/en/2.0.x/)

This project was developed to allowed people to store their notes in your personal account.

The main files are:
* views.py
* auth.py
* notes.py

### [views.py](https://github.com/OldemarJesus/python-login-system/blob/main/website/views.py)
Trait the action on the profile page of the user

### [auth.py](https://github.com/OldemarJesus/python-login-system/blob/main/website/auth.py)
Work with all action about de **login**, **register** and **logout**

### [notes.py](https://github.com/OldemarJesus/python-login-system/blob/main/website/notes.py.py)
Perform the action of **add** a note or **delete** them

All this file are register on de [`` __init__.py ``](https://github.com/OldemarJesus/python-login-system/blob/main/website/__init__.py) file located on the website folder.

In this project is using the [***sqlite database***](https://www.sqlite.org/index.html) to store data and [***flask_login***](https://flask-login.readthedocs.io/en/latest/) to trait session of the user
