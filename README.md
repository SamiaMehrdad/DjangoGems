# DjangoGems
A Django / Python showcase project, built step by step, from scratch.
---
### STEP 1:
Following official Django documents to create Django starter app:

`$ django-admin startproject djangoGems`  
`$ python3 manage.py startapp main_app`

 And creteaing our gems database in Postgresql 
`$ createdb gems`

Sure then running local server:
`$ python3 manage.py startapp main_app`

---
### STEP 2:
Updating `settings.py` to use my Postresql, germs

And migrating data `python3 manage.py migrate` 

---
### STEP 3:
One time URL setup:

`touch main_app/urls.py`

And edit djangoGems project's `urls.py` to re-route all incoming paths to this new URL mapper.

---
### STEP 4:
Defining `Home` route and related `view` function, edit `/main-app/view.py`

---
### STEP 5:
Using Django Templates.

`$ mkdir main_app/templates`