To launch Django, click RUN and then execute the following commands in the CONSOLE or SHELL:

django-admin startproject mysite
cd mysite

In the IDE, locate file mysite/settings.py and update:
ALLOWED_HOSTS = ["*"]

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8080

To access the running server:
- hover your mouse over OPEN DESKTOP, copy the instance URL, and paste it in a new tab
- in your Browser address bar to see your running app on port 8080.