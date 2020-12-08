# Fanprime

There are two endpoints:
* /search : search a user from API twitch
* /credential : store your app credentials

## Set up your environment

```
$ docker-compose run web django-admin startproject my-project .
$ docker-compose run web django-admin startapp my-app

# To give rights to django-admin files
$ sudo chown -R $USER:$USER .

$ docker-compose run web python manage.py migrate
$ docker-compose up -d

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
## Steps to build this project

* 1 - Create a developer account for twitch API
* 2 - Create an app to get client id and client secret
* 3 - Develop a python script to get information of a user
* 4 - Create the API
* 5 - Integrate python script in API
* 6 - Create a front with a form
