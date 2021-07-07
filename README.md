# storefront
A simple store project to learn Django

- mockaroo.com -> generate mock data
- django queryset api -> to find all keywords for filtering data
- 

============================================================================
VS.CODE Shortcuts
- Ctrl + T -> go to file
- Ctrl + shift + P -> command executer
- Ctrl + shift + M -> problems
- Ctrl + shift + O -> go to symbol in file

============================================================================
- pip install pipenv
- pipenv install -> creates virtual environment and installs all dependencies 
- pipenv install django
- pipenv shell
- django-admin startproject [appname] .    -> . means not to create another directory for package and use the current directory
- python manage.py runserver [port-number] -> port-number is optional. Default is 8000. manage.py is a wrapper around django-admin api

* for vscode terminal, should cofigure the interpreter to use the app virtual environment:
- Ctrl + shift + P -> select interpreter -> Enter the env path + /bin/python
- pipenv --venv -> get venv info


- python manage.py startapp [app-name] -> create app. Then add the appname to settings.py -> INSTALLED_APPS = []

- python manage.py makemigrations [appname] [--empty] -> [--empty] creates an empty migration file
- python manage.py migrate [appname] [migration-sequence-number] -> if not provide options, all migrations will apply for all apps to their latest available migration file
- python manage.py sqlmigrate [appname] [migration-sequence-number]

