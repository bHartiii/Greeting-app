# Greeting App

### Pre-requirements for the project:

    1. python - version: 3.7.7  

### Installation of mongodb on system:

* For Windows:
    1. Download the installer.
        - Download the MongoDB Community .msi installer from the following link:
            https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.2-signed.msi

            In the Version dropdown, select the version of MongoDB to download.
            In the Platform dropdown, select Windows.
            In the Package dropdown, select msi.
            Click Download.
    2. Run the MongoDB installer.
    3. Configure system enviornment variables for mogodb
    4. Run the mongodb server by using following command in cmd:
        - mongo.exe

* For Ubuntu follow this link:
    1. Import the public key used by the package management system.
    From a terminal, issue the following command to import the MongoDB public GPG Key from https://www.mongodb.org/static/pgp/server-4.4.asc:
    - wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
    The operation should respond with an OK.
    2. Create a list file for MongoDB.
        Create the list file /etc/apt/sources.list.d/mongodb-org-4.4.list for your version of Ubuntu.
    3. Create the /etc/apt/sources.list.d/mongodb-org-4.4.list file for Ubuntu 20.04 (Focal):
        - echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
    4. sudo apt-get update
    5. sudo apt-get install -y mongodb-org
    6. sudo systemctl start mongod
    
###  Create project directory and create virtual enviornment there:

* Open prject directory using git bash :
    - virtualenv venv
    - cd venv\Scripts
    - . activate
    This will create activate the virtual enviornment name as venv.    

### Install django and create django project & app:

* After activating virtual enviornment go to project directory and run following commands:
    1. pip install django
    2. django-admin startproject greeting_app
    3. cd greeting_app
    4. python manage.py startapp greetingsApp

### Configuration of database with django project:

* Install djongo engine inside project directory:
    - pip install djongo
* Open settings.py:
    - Comment the deafult sqlite3 database mapping.
    - Add the following to it:

    ----
        DATABASES = {
        'default': {

            'ENGINE': 'djongo',
            'NAME' : 'DATABASE_NAME',
            }
        }
    ----

### Configuration of urls for greetingsApp:

* Add the following line to urls.py of greeting_app:

    ----
        path('', include('greetingsApp.urls')),
    ----
* Create a file as urls.py inside greetingsApp directory:
    - mkdir urls.py
    - Add the following code for routing of api of this app:

        ----
            from django.contrib import admin
            from django.urls import path
            from greetingsApp import views
        
            urlpatterns = [
                path('', views.index, name='index'),

            ]
        ----

### Create model to interact with database connected with this project:

* Create a class for a collection:

    ----
        class Users(models.Model):
        name = models.CharField(max_length=100)
        msg = models.CharField(max_length=100)
        date = models.DateTimeField(auto_now_add=True,db_index=True,)
    ----

### Register the model in admin.py

* Every model has to be registered like this:

    ----
        from django.contrib import admin
        from greetingsApp.models import Users

        admin.site.register(Users)
    ----

### Register the app in settings.py:

        INSTALLED_APPS = [
            'greetingsApp.apps.GreetingsappConfig',
        ....

### Migreation of databse and collections:

* To create superuser:-python manage.py createsuperuser()
* For migration of database:- python manage.py makemigrations
* To create object of model:- python manage.py migrate

### Template creation:
* Create a folder for templates inside project directory.
    - Configure template folder in settings.py:

        ---
            TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [ BASE_DIR / "templates"],
                ...
        ----

    - Use html tags and jinja template to create dynamic html pages.
    - First create a base template as base.html
        1. In this template the code for header and footer will be written.
        2. Demo of passing the dynamic title for different templates using jinja templating:

            ----
                <title>{% block title %}{% endblock title %}</title>
            ----

        3. Give csrf_token in template for security purpose.
    - Other templates will extend this base.html as base, so all pages will have same header and footer.

        ----
            {% extends 'base.html' %}
            {% block title %}
                Greeting Form
            {% endblock title %}
        ----

    - Create a form in index.html.
        1. Use POST method for create operation.
        2. Same code can be used for update.html
        3. Form should be inside body like:

            ----
                {% block body %}
                <div class="container" style="padding:5%">
                    <h1 class="text-center">Give your message here!!!</h1>
                    <form autocomplete="off" name="form" method="post" action = ""class="form" onsubmit=" return validateform()">
                        {% csrf_token %}

                        ...

                {% endblock body %}
            ----

    - Create a grid to display data from the database in show.html.

### Styling of templates:

* Create a folder for static data like css and js or images
* Config this static folder in settings.py:

    ----
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
    ----

* Create a different folder for css file and js files inside the static folder.
* use style tag to add external css sheet in base template.
* use script tag to add js files into base template.

### Create Api in views.py of greetingsApp to perform CRUD operations:

* Name of functions should be same as given in urls.py for routing:
- Example for create operation :
    
    ----
        def index(request):
            if request.method == 'POST':
                name = request.POST.get('name')
                msg = request.POST.get('msg')
                user = Users(name=name, msg=msg)
                try:
                    user.save()
                    messages.success(request, 'Your greeting is added!!!')
                except:
                    pass
                logger.info("New user is added to greeting database.")
                return redirect('/show')
            return render(request,'index.html')
    ----

### Run the server and check the output on localhost

* Command to run server: python manage.py runserver
* In browser go to localhost:8000

### Add Log file to record the interactions with app:

* Create a folder for log file
* Create a log file greeting.log inside the log folder.
* Configuration of greeting.log in setting.py:

    -----
        LOGGING = {
            'version':1, 
            'loggers' : {
                'django' : {
                    'handlers':['file'],
                    'level' : 'DEBUG'
                }
            },
            'handlers' : {
                'file': {
                    'level': 'INFO',
                    'class':'logging.FileHandler',
                    'filename':'./logs/greetings.log',
                    'formatter':'simple',
                }
            },
            'formatters':{
                'simple':{
                    'format': '{levelname} {asctime} {module} {message}',
                    'style': '{'
                }
            }
        }
    -----