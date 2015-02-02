# How to use it

1. activate virtualenv
1. `Install Django 1.7 ($ pip install Django>=1.7)`
1. `$ django-admin.py startproject --template https://github.com/kmollee/django-project-template/zipball/master projectname`
1. `cd projectname`
1. `pip install -r requirements/dev.txt`
1. `$ python manage.py syncdb`
1. `$ python manage.py migrate`
1. `$ python manage.py runserver`
