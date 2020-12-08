from django.db import models


class Credential(models.Model):
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
