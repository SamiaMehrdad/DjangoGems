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

`$ mkdir main_app/templates`<br>
`touch main_app/templates/about.html`

---
### STEP 6:
Using template Inheritance (Partials)

`$ touch main_app/templates/base.html`

Use [Django template tags](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#ref-templates-builtins-tags) to extend `About` page from `Base` page.

---
### STEP 7:
Including Static Files in a Template

`$ mkdir main_app/static/css`<br>
`$ touch main_app/static/css/style.css`

---
### STEP 8:
Render Data in a Template

Make model in models.py, then template.

`$ mkdir main_app/templates/gems`<br>
`$ touch main_app/templates/gems/index.html`