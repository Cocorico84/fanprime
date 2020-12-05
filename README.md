# fanprime



## How to launch docker-compose in background

```
docker-compose up -d
```

## If you want to reuse docker-compose yaml

### Create a django project
```
docker-compose run web django-admin startproject my-project .
```

### Create an app
```
docker-compose run web django-admin startapp my-app
```

### Give rights to django-admin files
```
sudo chown -R $USER:$USER .
```

### Settings.py
```
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
