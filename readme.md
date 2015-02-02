# How to use it

1. `Install Django 1.7 ($ pip install Django>=1.7)`
1. `$ django-admin.py startproject --template https://github.com/kmollee/django-project-template/zipball/master projectname`
1. `$ cd projectname`
1. `$ ./virtualenv.sh`
1. '$ source ./env/bin/activate'
1. `$ cd ./source`
1. set up database in etc's settings folder(`dev.py`)
1. `$ ./manage.py syncdb`
1. `$ ./manage.py migrate`
1. `$ ./manage.py runserver`
