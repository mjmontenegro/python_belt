
# Flash
from flask import flash

flash("Test Message")

in html:
# {% with messages = get_flashed_messages() %}     <!-- declare a variable called messages -->
#     {% if messages %}                            <!-- check if there are any messages -->
#         {% for message in messages %}            <!-- loop through the messages -->
#             <p>{{message}}</p>                   <!-- display each message in a paragraph tag -->
#         {% endfor %}
#     {% endif %}
# {% endwith %}



# Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
bcrypt.generate_password_hash(password_string) # => save to database
bcrypt.check_password_hash(hashed_password, password_string) # compare hashed password to inputted password

# regex
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
if not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid email address")

# django setup
# turn on virtual env and start a new django project
# django-admin startproject your_project_name_here
# test the setup
# in your_project_name/python manage.py runserver
# manually create a folder for your projects apps
# in your_project_name/ mkdir apps
# for every app you add to your project you should do the following
# in your_project_name/apps python ../manage.py startapp your_app_name_here
# create an empty urls.py for your app in its own directory
# in your_project_name/apps/your_app_name_here touch urls.py
# add the app to the settings.py of the project
# in your_project_name/your_project_name/settings.py add "'apps.your_app_name_here'," to the installed_apps list

# creating a "/" route
# add a url pattern for your app in the project level urls.py that point to the apps level urls.py
# in your_project_name/your_project_name/urls.py add ", include" to imports and "url(r'^', include('apps.your_app_name_here.urls'))," to urlpatterns list
# add the routes your want your app to handle to your app level urls.py
# in your_project_name/apps/your_app_name_here/urls.py add a url pattern i.e. "url(r'^$', views.index)," and "from . import views" and "from django.conf.urls import url"
# # then actually put a funcion for that route called index in our apps view file
# in your_project_name/apps/your_app_name_here/views.py add "from django.shortcuts import render, HttpResponse" and "def index(request):" and "return HttpResponse("this is the equivalent of @app.route('/')!)"

# 1 create project. 2 create app folder, app, and url.py for app.  3 add app to project settings.py and app route to urls.py
# 4 add app routes to apps url.py and app methods to app views.py

# datetimens
from datetime import datetime
#datetime class python 
time_delta = datetime.now() - onemessage['created_at']
print(timedelta.d) # for days

# django shell
# in project directory "python manage.py" shell
# type "from apps.your_app_name_here.models import *"

# url patterns
# url(r'^bears$', views.one_method),                        # would only match localhost:8000/bears
# url(r'^bears/(?P<my_val>\d+)$', views.another_method),    # would match localhost:8000/bears/23
# url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),    # would match localhost:8000/bears/pooh/poke
# url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),  # would match localhost:8000/17/brown

# ORM Models
# from django.db import models
    
# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __repr__(self):
#         return f"<Movie object: {self.title} ({self.id})>"

# Migrations
# "python manage.py makemigrations" then "python manage.py migrate" in the project directory

# ORM CRUD
# ClassName.objects.create(field1="value for field1", field2="value for field2",etc.)
# can use auto_nfow_add=True or auto_now=True as parameters to time fields
# methods that return one instance: first(), last(), get(id=1) *throws error unless there is one and only one record
# methods that return multiple instances: all(), filter(field1="value for field 1", etc.), exclude(field1="value")
# updating a record: {selected record}.field_name = "value", {selected record}.save()
# deleteing a record: .delete() on record
# displaying records as a single dictionary of values .__dict__
# .values() shows all the values of a query set
# ordering: .order_by("field_name") or .order_by("-field_name")

# ORM One to Many
# create field in model with foreighn key info and related name
# author = models.ForeignKey( Author, related_name = "books")
# can access related name with some_author.books.all()

# ORM Many to Many
# create field in model with many to many field and related name
# books = models.ManyToManyField(Book, related_name="publishers")
# it doesn't matter what model has this key
# use use this_publisher.books.add(this_book) or this_book.publishers.add(this_publisher)
# use remove() to remove the relationship
# this_publisher.books.all() or this_book.publishers.all() to see all books/pubishers for a given book/publisher

# for book in Book.objects.filter(id__lte=3): 

# in views make sure to put "from .models import Movie"

# release_date.strftime('%Y-%m-%d')

# from datetime import datetime
#strptime .seconds


# static files: {{ load static}} then <script src="{% static 'shows_app/js/script.js' %}"></script>

# views.py should have from __future__ import unicode_literals



# deployment - our end
1) enter virtual env
2) pip freeze > requirements.txt
3) remove pygraphviz, pydot, and anything with mysql from file
4) in the project directory touch .gitignore
5) add "__pycache__/", ".vscode/", "venv/" and "db.sqlite3" to the file
6) "git init", "git add --all", git commit -m "initial commit"
7) create new repo on github and run "git remote add origin https://..." and "git push origin master"

# deployment - server
1) sudo apt-get update
2) sudo add-apt-repository ppa:jonathonf/python-3.6
3) sudo apt-get update
4) sudo apt-get install python3.6 -y
5) sudo apt-get install python-pip python3.6-dev nginx git -y
6) sudo apt-get update
7) sudo pip install virtualenv
8) git clone https:/...
9) in repo name directory do the following: "virtualenv venv --python=python3.6" "source venv/bin/activate"
10) in repo dir: "pip install -r requirements.txt"


# change project
# clone new repo
# install venv in repo directory and install requirements.txt, django, etc
# ~/myRepoName$ virtualenv venv --python=python3.6 ...

# update settings.py for project to add allowed hosts and static root and then collect static
# "ALLOWED_HOSTS = ['{{yourEC2.public.ip}}']" and "STATIC_ROOT = os.path.join(BASE_DIR, "static/")"
# python manage.py collectstatic
# change gunicorn service file

# setup new nginx file for project and change symbolic link



ssh -i "ecs_key1.pem" ubuntu@ec2-18-217-219-88.us-east-2.compute.amazonaws.com
18.217.219.88


/sbin/shutdown -r now OR sudo reboot


